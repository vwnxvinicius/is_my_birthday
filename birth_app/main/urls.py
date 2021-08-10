from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("birth",views.get_day, name="index")
]
