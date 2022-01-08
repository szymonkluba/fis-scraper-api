from django.urls import path

from . import views

urlpatterns = [
    path("scrap_race/", views.ScrapRace.as_view()),
]
