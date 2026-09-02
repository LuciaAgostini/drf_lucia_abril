from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Saludo
from .serializers import SaludoSerializer


@api_view(["GET", "POST"])
def saludo_list(request):
    """
    GET  -> Lista todos los saludos.
    POST -> Crea un nuevo saludo.
    """
    if request.method == "GET":
        saludos = Saludo.objects.all()
        serializer = SaludoSerializer(saludos, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = SaludoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def saludo_detail(request, pk):
    """
    GET    -> Devuelve el detalle de un saludo.
    PUT    -> Actualiza un saludo por completo.
    PATCH  -> Actualiza un saludo parcialmente.
    DELETE -> Elimina un saludo.
    """
    saludo = get_object_or_404(Saludo, pk=pk)

    if request.method == "GET":
        serializer = SaludoSerializer(saludo)
        return Response(serializer.data)

    if request.method in ("PUT", "PATCH"):
        parcial = request.method == "PATCH"
        serializer = SaludoSerializer(saludo, data=request.data, partial=parcial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        saludo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
