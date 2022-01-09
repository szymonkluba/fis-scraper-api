from django.urls import path

from . import views

urlpatterns = [
    path("scrap_race", views.ScrapRace.as_view()),
    path("list_folder", views.ListFolder.as_view()),
    path("list_folder/<str:path>", views.ListFolder.as_view()),
    path("download/file", views.DownloadFile.as_view()),
    path("download/folder", views.DownloadFolder.as_view()),
    path("download/current", views.DownloadCurrentFiles.as_view())
]
