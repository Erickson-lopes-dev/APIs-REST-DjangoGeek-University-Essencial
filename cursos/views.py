from rest_framework import generics
from rest_framework.generics import get_object_or_404

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

    def get_queryset(self):
        # se algum parâmetro "curso_pk" for passado...
        if self.kwargs.get('curso_pk'):
            # Retorna o curso encontrado com o pk
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        # Se não, retorna todos os cursos
        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avalicacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        # se algum parâmetro "curso_pk" for passado...
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(),
                                     # procura um curso pk com o parâmetro passado
                                     curso_id=self.kwargs.get('curso_pk'),
                                     # procura uma avaliazao pk com o parâmetro passado
                                     pk=self.kwargs.get('avaliacao_pk'))

        # caso contrario só procura um pk especificado
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))

