from django.urls import path
from .views import landing_page, start_investing, register_startup

urlpatterns = [
    path("", landing_page, name="landing_page"),
    path("start_investing/", start_investing, name="start_investing"),
    path("register_startup/", register_startup, name="register_startup"),
]
