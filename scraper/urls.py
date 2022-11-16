from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views


router = SimpleRouter()
router.register("scrap_race", views.ScrapRaceViewSet, basename="scrap-race")
router.register("download", views.DownloadViewSet, basename="download")
router.register("race", views.RaceViewSet, basename="race")

urlpatterns = [
    path("", include(router.urls)),
]
