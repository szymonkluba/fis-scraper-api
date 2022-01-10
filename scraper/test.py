from dropbox import Dropbox
from dropbox.exceptions import ApiError, BadInputError
from rest_framework import serializers
from stone.backends.python_rsrc.stone_validators import ValidationError

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
    try:
        file = dbx.files_download(path="/")
    except ApiError as e:
        print(e.error, e.user_message_text, e.user_message_locale)
    except ValidationError as e:
        print(e.message, e)
    except BadInputError as e:
        print(e, e.message)
