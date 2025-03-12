from django.urls import path
from .views import contact, landing_page

urlpatterns = [
    path("", landing_page, name="landing_page"),
    path("contact/", contact, name="contact"),
]
