from django.urls import path

from . import views

urlpatterns = [
    path("saludos/", views.saludo_list, name="saludo-list"),
    path("saludos/<int:pk>/", views.saludo_detail, name="saludo-detail"),
]
