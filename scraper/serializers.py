from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework import serializers

from scraper.constants import FLAT_JSON_RESPONSE
from scraper.mixins import FlattenMixin
from scraper.models import (
    Race,
    Tournament,
    Participant,
    Jumper,
    Country,
    ParticipantCountry,
    Jump,
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


class CountrySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    fis_code = serializers.IntegerField(allow_null=True)

    def create(self, validated_data):
        country, _ = Country.objects.get_or_create(name=validated_data["name"])
        return country

    def update(self, instance, validated_data):
        country = Country.objects.update(name=validated_data["name"])
        return country


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


class JumperSerializer(serializers.Serializer):
    fis_code = serializers.IntegerField()
    born = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    nation = CountrySerializer()

    def update(self, instance, validated_data):
        print(validated_data)
        name = validated_data["name"].split()
        name[0] = name[0].upper()
        name = name.join(" ")
        country, _ = Country.objects.get_or_create(
            name=validated_data["nation"]["name"].split().
        )
        jumper = Jumper.objects.update(
            name=name,
            fis_code=validated_data["fis_code"],
            born=validated_data["born"],
        )
        jumper.nation = country
        jumper.save()
        return jumper

    def create(self, validated_data):
        print(validated_data)
        name = validated_data["name"].split()
        name[0] = name[0].upper()
        name = name.join(" ")
        country, _ = Country.objects.get_or_create(
            name=validated_data["nation"]["name"]
        )
        jumper = Jumper.objects.create(
            name=name,
            fis_code=validated_data["fis_code"],
            born=validated_data["born"],
        )
        jumper.nation = country
        jumper.save()
        return jumper


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


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Example flat race",
            summary="Flatten JSON race response",
            description="Response with flatten nested objects of participants",
            value=FLAT_JSON_RESPONSE,
            response_only=True,
        )
    ]
)
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


class TableSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    url = serializers.URLField()
