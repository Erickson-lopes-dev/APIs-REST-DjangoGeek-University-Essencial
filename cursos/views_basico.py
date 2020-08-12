# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Curso, Avalicacao
# from .serializers import CursoSerializers, AvaliacaoSerializer
#
#
# class CursoAPIView(APIView):
#     """
#     API de cursos da Geek
#     """
#     # se a requisição for get
#     def get(self, request):
#         cursos = Curso.objects.all()
#         # many=True, quando for todos os dados / converte os items para json
#         serializer = CursoSerializers(cursos, many=True)
#         # retorna os itens convertidos como resposta
#
#         print(request.data)  # recebe dados
#         print(request.user)
#         print(request.query_params)
#
#         return Response(serializer.data)
#
#     def post(self, request):
#         # Pega od valores recebidos em json convertendo para o python ler
#         serializer = CursoSerializers(data=request.data)
#
#         # Verifica se os dados são validos
#         serializer.is_valid(raise_exception=True)
#
#         # Salva os dados
#         serializer.save()
#
#         # Retorna os dados recebidos com o status de 201
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         # Mensagem personalizada de retorno
#         # return Response({"msg": "Criou com sucesso"}, status=status.HTTP_201_CREATED)
#
#         # retornando somento o item especificado
#         # return Response({"id": serializer.data['id'], "titulo": serializer.data['titulo']},
#         #                 status=status.HTTP_201_CREATED)
#
#
# class AvaliazaoAPIView(APIView):
#     """
#     API de avaliações da Geek
#     """
#
#     def get(self, request):
#         avaliacoes = Avalicacao.objects.all()
#         serializer = AvaliacaoSerializer(avaliacoes, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = AvaliacaoSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)