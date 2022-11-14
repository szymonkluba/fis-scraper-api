from django.http import FileResponse
from django.shortcuts import render
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.decorators import schema, action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from .dropbox_utils import get_file_data, list_folder, download_file, download_folder
from .exceptions import InvalidDataProvided
from .models import Race
from .serializers import (
    ScrapRaceSerializer,
    FolderSerializer,
    FileMetadataSerializer,
    RaceDetailsSerializer,
    RaceListSerializer,
    MetaRaceSerializer,
    FlatDataRaceSerializer,
)
from .utils import get_file, Website, generate_raw_participants


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
        responses=MetaRaceSerializer,
    )
    def create(self, request):
        """
        Scrap single race and return Dropbox file metadata.
        """

        serializer = ScrapRaceSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            race = serializer.save()
            file_metadata = FileMetadataSerializer(get_file_data(race))
            return Response(
                {
                    "fis_id": validated_data.get("fis_id"),
                    "details": validated_data.get("details"),
                    **file_metadata.data,
                }
            )

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
        responses=OpenApiTypes.BINARY,
    )
    @action(detail=False, methods=["post"])
    def csv(self, request):
        """
        Scrap single race and return race details in csv file.
        """
        serializer = ScrapRaceSerializer(data=request.data)
        if serializer.is_valid():
            race = serializer.save()
            filename = str(race).replace(" ", "_")
            race = FlatDataRaceSerializer(race)
            file, filename = get_file(race.data, filename)

            return FileResponse(file, filename=filename, as_attachment=True)

        raise InvalidDataProvided

    @extend_schema(request=ScrapRaceSerializer, responses=OpenApiTypes.BINARY)
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


class FolderViewSet(ViewSet):
    """
    List content of folder on API's Dropbox. If path is not provided list contents of base folder.
    """

    serializer_class = FolderSerializer
    lookup_field = "path"

    def get_object(self, path=""):
        return list_folder(path)

    def list(self, request):
        folder = self.get_object()
        serializer = FolderSerializer(folder)
        return Response(serializer.data)

    @extend_schema(
        parameters=[
            OpenApiParameter(name="path", type=OpenApiTypes.STR, location="path")
        ]
    )
    def retrieve(self, request, path=None):
        folder = self.get_object(f"/{path}" if path else "")
        serializer = FolderSerializer(folder)
        return Response(serializer.data)


class DownloadViewSet(ViewSet):
    @extend_schema(request=FileMetadataSerializer, responses=OpenApiTypes.BINARY)
    @action(detail=False, methods=["post"])
    def file(self, request):
        """
        Download file from API's Dropbox.
        """

        file_metadata = FileMetadataSerializer(data=request.data)
        if file_metadata.is_valid():
            file, filename = download_file(file_metadata.validated_data.get("id"))
            return FileResponse(file, filename=filename, as_attachment=True)

    @extend_schema(request=FileMetadataSerializer, responses=OpenApiTypes.BINARY)
    @action(detail=False, methods=["post"])
    def folder(self, request):
        """
        Download folder from API's Dropbox (as .zip file).
        """

        folder_metadata = FileMetadataSerializer(data=request.data)
        if folder_metadata.is_valid():
            file, filename = download_folder(folder_metadata.validated_data.get("id"))
            return FileResponse(file, filename=filename, as_attachment=True)

    @extend_schema(request=FolderSerializer, responses=OpenApiTypes.BINARY)
    @action(detail=False, methods=["post"])
    def current(self, request):
        """
        Download specified files from API's Dropbox (as .zip file).
        """

        folder_metadata = FileMetadataSerializer(data=request.data)
        if folder_metadata.is_valid():
            file, filename = download_folder(folder_metadata.validated_data.get("id"))
            return FileResponse(file, filename=filename, as_attachment=True)


@schema(None)
class WakieWakie(APIView):
    def get(self, request):
        return Response("Server is up")
