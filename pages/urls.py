from django.urls import path
from pages import views

url_patterns = [
    path("", views.home, name="home")
]