from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path("admin/", admin.site.urls, name="scraper-admin"),
    path("api/", include("scraper.urls"), name="scraper-api"),
    path("openapi/", SpectacularAPIView.as_view(), name="openapi-schema"),
    path(
        "openapi/swagger/",
        SpectacularSwaggerView.as_view(url_name="openapi-schema"),
        name="swagger",
    ),
    path(
        "openapi/redoc",
        SpectacularRedocView.as_view(url_name="openapi-schema"),
        name="redoc",
    ),
]
