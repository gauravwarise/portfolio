from django.contrib import admin
from django.urls import path
from .views import HomeVie

urlpatterns = [
    path('',HomeVie.as_view(), name="home"),
]