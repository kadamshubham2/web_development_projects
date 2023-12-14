from django.contrib import admin
from django.urls import path, include
from .views import UserSignupForm

urlpatterns = [
    path('register/', UserSignupForm.as_view(), name='register')
]