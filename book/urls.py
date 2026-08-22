from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render,redirect
from . import views
app_name = "book"

urlpatterns = [
    path("login",views.loginView, name="login_view")
]