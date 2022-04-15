from django.contrib import admin
from django.urls import path
from booktime.main.views import about, home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("about/", about, name="about"),
]
