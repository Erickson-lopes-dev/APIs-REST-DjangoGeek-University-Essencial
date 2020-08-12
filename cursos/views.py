from rest_framework import generics

from .models import Curso, Avalicacao
from .serializers import CursoSerializers, AvaliacaoSerializer


class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializers


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializers


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avalicacao.objects.all()
    serializer_class = AvaliacaoSerializer


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avalicacao.objects.all()
    serializer_class = AvaliacaoSerializer
