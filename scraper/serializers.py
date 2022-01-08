from rest_framework import serializers

from scraper.models import Race
from scraper.utils import get_race


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = ['fis_id', 'place', 'tournament', 'date', 'kind', 'hill_size', 'details']

    date = serializers.DateTimeField(format="%Y-%m-%d")
    tournament = serializers.SlugRelatedField("name", many=False, read_only=True)


class ScrapRaceSerializer(serializers.Serializer):
    fis_id = serializers.IntegerField()
    details = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return get_race(**validated_data)

    def update(self, instance, validated_data):
        pass
