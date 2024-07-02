from django.contrib import admin
from django.urls import re_path, include
from . import views

urlpatterns = [
    re_path(r'^api/v1/data/sendData', views.DataView.as_view()),
    re_path(r'^api/v1/data/getData', views.DataView.as_view()),
]