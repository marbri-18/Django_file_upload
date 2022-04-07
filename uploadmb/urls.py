from django.urls import path
from . import views

app_name = "uploadmb"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("upload", views.upload, name="upload")
]