from django.contrib import admin
from .models import *


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    pass


@admin.register(ParticipantCountry)
class ParticipantCountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    pass


@admin.register(Jumper)
class JumperAdmin(admin.ModelAdmin):
    pass


@admin.register(Jump)
class JumpAdmin(admin.ModelAdmin):
    pass


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    pass

