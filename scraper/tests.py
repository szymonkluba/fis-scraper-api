from django.urls import reverse, path, include
from rest_framework.test import APITestCase

from scraper.views import ScrapRaceViewSet


class ScrapRaceTests(APITestCase):
    urlpatterns = [path("api/", include("scraper.urls"))]

    view = ScrapRaceViewSet.as_view()

    def test_scrap_race(self):

        url = self.view.reverse_action(self.view.create.name)
        print(url)
