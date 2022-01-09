from django.http import Http404, FileResponse
from dropbox.exceptions import ApiError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .dropbox_utils import get_file_data, list_folder, download_file, download_folder, download_current_files
from .serializers import ScrapRaceSerializer, FolderSerializer, FileMetadataSerializer
from .utils import RaceNotFound


class ScrapRace(APIView):

    def post(self, request, format=None):
        serializer = ScrapRaceSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            try:
                race = serializer.save()
            except RaceNotFound:

                return Response({
                    "fis_id": validated_data.get("fis_id"),
                    "details": validated_data.get("details"),
                    "status": "error"
                }, status=status.HTTP_404_NOT_FOUND)

            file_status = get_file_data(race)

            return Response({
                "fis_id": validated_data.get("fis_id"),
                "details": validated_data.get("details"),
                "id": file_status.id,
                "name": file_status.name,
                "path_lower": file_status.path_lower,
                "path_display": file_status.path_display,
                "status": "success",
            })

        return Response({
            "fis_id": serializer.initial_data.get("fis_id"),
            "details": serializer.initial_data.get("details"),
            "status": "error"
        }, status=status.HTTP_400_BAD_REQUEST)


class ListFolder(APIView):

    def get_object(self, path):
        try:
            return list_folder(path)
        except ApiError:
            raise Http404

    def get(self, request, path=None, format=None):
        if path is not None:
            folder = self.get_object(f"/{path}")
        else:
            folder = self.get_object("")
        serializer = FolderSerializer(folder)
        return Response(serializer.data)


class DownloadFile(APIView):

    def post(self, request):
        file_metadata = FileMetadataSerializer(data=request.data)
        if file_metadata.is_valid():
            file = download_file(file_metadata.validated_data.get("id"))
            return FileResponse(file)


class DownloadFolder(APIView):

    def post(self, request):
        folder_metadata = FileMetadataSerializer(data=request.data)
        if folder_metadata.is_valid():
            file, filename = download_folder(folder_metadata.validated_data.get("id"))
            return FileResponse(file, filename=filename)


class DownloadCurrentFiles(APIView):

    def post(self, request):
        current_files = FolderSerializer(data=request.data)
        if current_files.is_valid():
            file, filename = download_current_files(current_files.validated_data.get("entries"))
            return FileResponse(file, filename=filename)
