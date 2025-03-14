from django.urls import path
from .views import landing_page, start_investing

urlpatterns = [
    path("", landing_page, name="landing_page"),
    path("start-investing/", start_investing, name="start_investing"),
]
