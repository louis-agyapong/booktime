from django.urls import path
from booktime.main.views import contact, home, about

app_name = "main"

urlpatterns = [
    path("", home, name="index"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
]
