from django.urls import path
from lab1app import views

urlpatterns = [
    path("", views.home, name="home"),
]