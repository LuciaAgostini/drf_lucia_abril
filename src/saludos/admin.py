from django.contrib import admin

from .models import Saludo


@admin.register(Saludo)
class SaludoAdmin(admin.ModelAdmin):
    list_display = ("mensaje", "autor", "idioma", "creado")
    search_fields = ("mensaje", "autor")
    list_filter = ("idioma",)
