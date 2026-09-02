from django.db import models


class Saludo(models.Model):
    mensaje = models.CharField(max_length=200)
    autor = models.CharField(max_length=100, blank=True)
    idioma = models.CharField(max_length=30, default="es")
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-creado"]

    def __str__(self):
        return f"{self.mensaje} ({self.idioma})"
