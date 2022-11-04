from django.http import FileResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .dropbox_utils import get_file_data, list_folder, download_file, download_folder, download_current_files
from .exceptions import InvalidDataProvided
from .serializers import ScrapRaceSerializer, FolderSerializer, FileMetadataSerializer


class ScrapRace(APIView):

    def post(self, request, format=None):
        serializer = ScrapRaceSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            race = serializer.save()
            file_metadata = FileMetadataSerializer(get_file_data(race))
            return Response({
                "fis_id": validated_data.get("fis_id"),
                "details": validated_data.get("details"),
                **file_metadata.data,
            })

        raise InvalidDataProvided


class ListFolder(APIView):

    def get_object(self, path):
        return list_folder(path)

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
            file, filename = download_file(file_metadata.validated_data.get("id"))
            return FileResponse(file, filename=filename, as_attachment=True)


class DownloadFolder(APIView):

    def post(self, request):
        folder_metadata = FileMetadataSerializer(data=request.data)
        if folder_metadata.is_valid():
            file, filename = download_folder(folder_metadata.validated_data.get("id"))
            return FileResponse(file, filename=filename, as_attachment=True)


class DownloadCurrentFiles(APIView):

    def post(self, request):
        current_files = FolderSerializer(data=request.data)
        if current_files.is_valid():
            file, filename = download_current_files(current_files.validated_data.get("entries"))
            return FileResponse(file, filename=filename, as_attachment=True)

class WakieWakie(APIView):

    def get(self, request):
        return Response("Server is up")