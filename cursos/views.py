from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Curso, Avalicacao
from .serializers import CursoSerializers, AvaliacaoSerializer


class CursoAPIView(APIView):
    """
    API de cursos da Geek
    """
    # se a requisição for get
    def get(self, request):
        cursos = Curso.objects.all()
        # many=True, quando for todos os dados / converte os items para json
        serializer = CursoSerializers(cursos, many=True)
        # retorna os itens convertidos como resposta

        print(request.data)
        print(request.user)
        print(request.query_params)

        return Response(serializer.data)


class AvaliazaoAPIView(APIView):
    """
    API de avaliações da Geek
    """

    def get(self, request):
        avaliacoes = Avalicacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
