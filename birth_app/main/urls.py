from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("birth",views.index, name="index"),
    path("isbirth", views.is_birth, name="isbirth"),
    path("notbirth", views.isnt_birth, name="notbirth"),
]
