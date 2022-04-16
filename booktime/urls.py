from django.contrib import admin
from django.urls import path, include
from booktime.main.views import about, home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("booktime.main.urls", namespace="main")),
]
