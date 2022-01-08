from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .dropbox_utils import get_file_data
from .serializers import ScrapRaceSerializer
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
