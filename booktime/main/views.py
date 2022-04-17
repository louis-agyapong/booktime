from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from booktime.main.forms import ContactForm


def home(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "main/index.html", context)


def about(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "main/about.html", context)


def contact(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_mail()
            return redirect("main:home")
    else:
        form = ContactForm()
    return render(request, "main/contact_form.html", {"form": form})
