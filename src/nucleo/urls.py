"""
Configuración de URLs del proyecto nucleo.
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path


def raiz(request):
    return redirect("saludo-list")


urlpatterns = [
    path("", raiz, name="raiz"),
    path("admin/", admin.site.urls),
    path("api/", include("saludos.urls")),
]
