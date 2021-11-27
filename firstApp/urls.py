from django.contrib import admin
from django.urls import path

from firstApp import views

urlpatterns = [
    path("", views.index),

    path("get-books", views.getBooks),
]