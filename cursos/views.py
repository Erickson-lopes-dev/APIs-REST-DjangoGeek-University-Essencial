from rest_framework import generics, mixins
from rest_framework.generics import get_object_or_404
from .models import Curso, Avalicacao
from .serializers import CursoSerializers, AvaliacaoSerializer

# v2
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

"""
API versão 1
"""


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


"""
API versão 2
"""


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializers

    # /avaliacoes/
    # Criar uma  nova rota quando método for get
    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        # Pega o curso atual
        curso = self.get_object()
        # busca todas as avaliações que o curso possui - related_name/ many para muitos
        # dentro do AvaliacaoSerializer vai pegar o curso e dentro de curso vai buscar todos
        serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
        # Retorna os itens coletados
        return Response(serializer.data)


# class AvaliacaoViewSet(viewsets.ModelViewSet):
#     queryset = Curso.objects.all()
#     serializer_class = AvaliacaoSerializer

# Pode colocar o tipo de opção que o usuario pode fazer como get, put ....
class AvaliacaoViewSet(mixins.CreateModelMixin,
                       # mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet,

                       ):
    queryset = Curso.objects.all()
    serializer_class = AvaliacaoSerializer
