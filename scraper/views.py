import datetime
import subprocess

import git
from django.http import FileResponse
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.decorators import schema, action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet

from .exceptions import InvalidDataProvided
from .files_utils import generate_file, pack_files, scrap_tables
from .models import Race, Jumper, Country
from .serializers import (
    ScrapRaceSerializer,
    FolderSerializer,
    RaceDetailsSerializer,
    RaceListSerializer,
    FlatDataRaceSerializer,
    JumperSerializer,
    CountrySerializer,
    TableSerializer,
)
from .utils import Website, generate_raw_participants


@schema(None)
class ApiRoot(APIView):
    def get(self, request, format=None, *args, **kwargs):
        return Response(
            {
                "races": reverse("list-races", request=request, format=format),
            }
        )


class RaceViewSet(ViewSet):
    queryset = Race.objects.prefetch_related(
        "participant_set", "participantcountry_set"
    )
    lookup_field = "uuid"

    @extend_schema(responses=RaceListSerializer)
    def list(self, request):
        """
        Returns list of all races.
        """

        queryset = Race.objects.all()
        serializer = RaceListSerializer(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data)

    @extend_schema(
        responses=RaceDetailsSerializer,
        parameters=[
            OpenApiParameter(name="uuid", type=OpenApiTypes.STR, location="path")
        ],
    )
    def retrieve(self, request, uuid=None):
        """
        Returns details of single race.
        """

        queryset = Race.objects.prefetch_related(
            "participant_set", "participantcountry_set"
        )
        race = get_object_or_404(queryset, uuid=uuid)
        serializer = RaceDetailsSerializer(race)
        return Response(serializer.data)

    @extend_schema(
        responses=FlatDataRaceSerializer,
        parameters=[
            OpenApiParameter(name="uuid", type=OpenApiTypes.STR, location="path")
        ],
    )
    @action(detail=True, methods=["get"])
    def flat_data(self, request, uuid=None):
        queryset = Race.objects.prefetch_related(
            "participant_set", "participantcountry_set"
        )
        race = get_object_or_404(queryset, uuid=uuid)
        serializer = FlatDataRaceSerializer(race)
        return Response(serializer.data)


class ScrapRaceViewSet(ViewSet):
    """
    Scrap single race.
    """

    queryset = Race.objects.prefetch_related(
        "participant_set", "participantcountry_set"
    )
    serializer_class = ScrapRaceSerializer

    @extend_schema(
        request=ScrapRaceSerializer,
        responses=RaceDetailsSerializer,
    )
    def create(self, request):
        """
        Scrap single race and return Dropbox file metadata.
        """

        serializer = ScrapRaceSerializer(data=request.data)
        if serializer.is_valid():
            race = serializer.save()
            generate_file(race)
            race_serializer = RaceListSerializer(race, context={"request": request})
            return Response(race_serializer.data)

        raise InvalidDataProvided

    @extend_schema(
        request=ScrapRaceSerializer,
        responses=RaceDetailsSerializer,
    )
    @action(detail=False, methods=["post"])
    def json(self, request):
        """
        Scrap single race and return race details in json format.
        """
        serializer = ScrapRaceSerializer(data=request.data)
        if serializer.is_valid():
            race = RaceDetailsSerializer(serializer.save())
            return Response(race.data)

        raise InvalidDataProvided

    @extend_schema(
        request=ScrapRaceSerializer,
        responses=FlatDataRaceSerializer,
    )
    @action(detail=False, methods=["post"])
    def flat_json(self, request):
        """
        Scrap single race and return race details in json format.
        """
        serializer = ScrapRaceSerializer(data=request.data)
        if serializer.is_valid():
            race = FlatDataRaceSerializer(serializer.save())
            return Response(race.data)

        raise InvalidDataProvided

    @extend_schema(
        request=ScrapRaceSerializer,
        responses={
            (201, "text/csv"): OpenApiTypes.BINARY,
            (201, "application/zip"): OpenApiTypes.BINARY,
        },
    )
    @action(detail=False, methods=["post"])
    def csv(self, request):
        """
        Scrap single race and return race details in csv file.
        """
        serializer = ScrapRaceSerializer(data=request.data)
        if serializer.is_valid():
            race = serializer.save()
            generate_file(race)
            filename = str(race).replace(" ", "_")

            return FileResponse(race.file.open(), filename=filename, as_attachment=True)

        raise InvalidDataProvided

    @extend_schema(
        request=ScrapRaceSerializer,
        responses={
            (201, "text/csv"): OpenApiTypes.BINARY,
        },
    )
    @action(detail=False, methods=["post"])
    def raw_data(self, request):
        serializer = ScrapRaceSerializer(data=request.data)
        if serializer.is_valid():
            website = Website(
                race_id=serializer.data.get("fis_id"),
                details=serializer.data.get("details", False),
            )
            filename = f"{website.get_race_place()}_{website.get_hill_size()}_{website.get_date()}{'_details' if website.details else ''}.csv"
            file = generate_raw_participants(website)
            return FileResponse(file, filename=filename, as_attachment=True)

        raise InvalidDataProvided


class DownloadViewSet(ViewSet):
    lookup_field = "uuid"

    @extend_schema(
        parameters=[
            OpenApiParameter(name="uuid", type=OpenApiTypes.STR, location="path")
        ],
        responses={
            (200, "text/csv"): OpenApiTypes.BINARY,
            (200, "application/zip"): OpenApiTypes.BINARY,
        },
    )
    @action(detail=True, methods=["get"])
    def file(self, request, uuid=None):
        """
        Download file.
        """

        queryset = Race.objects.prefetch_related(
            "participant_set", "participantcountry_set"
        )
        race = get_object_or_404(queryset, uuid=uuid)
        filename = str(race).replace(" ", "_")
        if not race.file:
            generate_file(race)
        file = race.file.open()
        return FileResponse(file, filename=filename, as_attachment=True)

    @extend_schema(
        request=FolderSerializer,
        responses={
            (201, "application/zip"): OpenApiTypes.BINARY,
        },
    )
    @action(detail=False, methods=["post"])
    def files(self, request):
        """
        Download files (as .zip file).
        """

        folder_metadata = FolderSerializer(data=request.data)
        if folder_metadata.is_valid():
            entries = map(
                lambda entry: entry.get("uuid"), folder_metadata.data.get("entries")
            )
            races = Race.objects.filter(uuid__in=entries, file__isnull=False)
            files = list(
                map(
                    lambda race: {"data": race.file, "filename": race.file.name},
                    list(races),
                )
            )

            zip_file = pack_files(files)
            filename = (
                datetime.datetime.now().isoformat(timespec="seconds").replace(":", "")
                + ".zip"
            )

            return FileResponse(zip_file, filename=filename, as_attachment=True)

        raise InvalidDataProvided


@extend_schema(
    responses={
        (201, "application/zip"): OpenApiTypes.BINARY,
    }
)
class ScrapTableViewSet(ViewSet):
    serializer_class = TableSerializer

    def create(self, request):
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid():
            file = scrap_tables(serializer.data.get("url"))
            return FileResponse(file, filename="tables.zip", as_attachment=True)

        raise InvalidDataProvided


class JumperViewSet(ModelViewSet):
    queryset = Jumper.objects.all()
    serializer_class = JumperSerializer
    lookup_field = "fis_code"


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = "name"


@schema(None)
class UpdateServerViewSet(ViewSet):
    def list(self, request):
        repo = git.Repo("~/fis-scraper-api")
        origin = repo.remotes.origin

        origin.pull()
        subprocess.run(["touch", "/var/www/www_fisscraper_online_wsgi.py"])
        return Response("Updated")
