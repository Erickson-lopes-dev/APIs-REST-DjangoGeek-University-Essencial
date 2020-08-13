from rest_framework import generics, mixins
from rest_framework.generics import get_object_or_404
from .models import Curso, Avalicacao
from .serializers import CursoSerializers, AvaliacaoSerializer

# v2
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# permissoes
from rest_framework import permissions
from .permissions import EhSuperUser
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
    # adicionando permissões, configuração pontual, Somente a permissão de django model spó com authenticados
    # pode adicionar e ler, gadastrando usuarios em grupos do django admin
    permission_classes = (
        EhSuperUser,  # verifica esse, importa a seguencia que esta colocando
        permissions.DjangoModelPermissions,
    )
    queryset = Curso.objects.all()
    serializer_class = CursoSerializers

    # /avaliacoes/
    # Criar uma  nova rota quando método for get
    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):

        # tamanho da página get recebida - avaliacoes em curso
        self.pagination_class.page_size = 2

        # buscando todas as avaliações do curso
        avaliacoes = Avalicacao.objects.filter(curso_id=pk)

        # dentro da query da paginação
        page = self.paginate_queryset(avaliacoes)

        # se tiver elemento na pagina
        if page is not None:
            # coloca na pagina as avaliacoes do curso e transforma em json para enviar
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # Pega o curso atual
        curso = self.get_object()

        # busca todas as avaliações que o curso possui - related_name/ many para muitos
        # dentro do AvaliacaoSerializer vai pegar o curso e dentro de curso vai buscar todos
        serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)

        # Retorna os itens coletados
        return Response(serializer.data)


# com todas as funções CRUD
# class AvaliacaoViewSet(viewsets.ModelViewSet):
#     queryset = Curso.objects.all()
#     serializer_class = AvaliacaoSerializer

# Pode colocar o tipo de opção que o usuario pode fazer como get, put ....
class AvaliacaoViewSet(mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet,

                       ):
    queryset = Avalicacao.objects.all()
    serializer_class = AvaliacaoSerializer
