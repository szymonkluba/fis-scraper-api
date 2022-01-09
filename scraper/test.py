from dropbox import Dropbox
from rest_framework import serializers

dbx = Dropbox("pXxtG3hvpq8AAAAAAAAAAQAdXmEGSVKSfHxnIx9pSP8qzJwq1I9iLVcyVI2GYZy1")


class FileMetadataSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    path_lower = serializers.CharField()
    path_display = serializers.CharField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class FolderSerializer(serializers.Serializer):
    entries = FileMetadataSerializer(many=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


if __name__ == '__main__':
    file = dbx.files_download(path="/Viessmann FIS Ski Jumping World Cup/Wisla_(POL)_HS134_2021-12-04.zip")
    print(file, type(file))
