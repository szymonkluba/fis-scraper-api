from rest_framework import serializers

from scraper.mixins import FlattenMixin
from scraper.models import (
    Race,
    Tournament,
    Participant,
    Jumper,
    Country,
    ParticipantCountry,
    Jump,
    Folder,
    FileMetadata,
)
from scraper.utils import get_race


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = [
            "fis_id",
            "place",
            "tournament",
            "date",
            "kind",
            "hill_size",
            "details",
        ]

    date = serializers.DateTimeField(format="%Y-%m-%d")
    tournament = serializers.SlugRelatedField("name", many=False, read_only=True)


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class ParticipantCountrySerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=False, read_only=True)

    class Meta:
        model = ParticipantCountry
        exclude = ["race"]


class FlatParticipantCountrySerializer(serializers.ModelSerializer):
    country = serializers.SlugRelatedField(read_only=True, slug_field="name")

    class Meta:
        model = ParticipantCountry
        exclude = ["race"]


class JumpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jump
        exclude = ["id"]


class JumperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jumper
        fields = "__all__"

    nation = CountrySerializer(read_only=True)


class FlatJumperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jumper
        exclude = ["id"]

    nation = serializers.SlugRelatedField(read_only=True, slug_field="name")


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = "__all__"


class ParticipantSerializer(serializers.ModelSerializer):
    jump_1 = JumpSerializer(read_only=True)
    jump_2 = JumpSerializer(read_only=True)
    jumper = JumperSerializer(read_only=True)

    class Meta:
        model = Participant
        exclude = ["race"]


class RaceDetailsSerializer(serializers.ModelSerializer):
    tournament = TournamentSerializer(read_only=True)
    participantcountry_set = ParticipantCountrySerializer(many=True, read_only=True)
    participant_set = ParticipantSerializer(many=True, read_only=True)

    class Meta:
        model = Race
        fields = [
            "uuid",
            "fis_id",
            "place",
            "tournament",
            "date",
            "kind",
            "hill_size",
            "details",
            "participant_set",
            "participantcountry_set",
        ]


class FlatParticipantSerializer(FlattenMixin, serializers.ModelSerializer):
    class Meta:
        model = Participant
        exclude = ["race", "jumper", "jump_1", "jump_2"]
        flatten = [
            ("jumper", FlatJumperSerializer),
            ("jump_1", JumpSerializer),
            ("jump_2", JumpSerializer),
        ]


class FlatDataRaceSerializer(RaceDetailsSerializer):
    participantcountry_set = FlatParticipantCountrySerializer(many=True, read_only=True)
    participant_set = FlatParticipantSerializer(many=True, read_only=True)

    class Meta:
        model = Race
        exclude = ["uuid"]


class RaceListSerializer(serializers.ModelSerializer):
    tournament = TournamentSerializer(read_only=True)

    class Meta:
        model = Race
        fields = "__all__"


class ScrapRaceSerializer(serializers.Serializer):
    fis_id = serializers.IntegerField()
    details = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return get_race(**validated_data)

    def update(self, instance, validated_data):
        pass


class FileSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    uuid = serializers.UUIDField()


class FolderSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    entries = FileSerializer(many=True)
