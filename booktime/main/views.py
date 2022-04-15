from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def home(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "main/index.html", context)


def about(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "main/about.html", context)
