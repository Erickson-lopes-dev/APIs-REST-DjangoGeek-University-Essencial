from rest_framework import serializers
from .models import Curso, Avalicacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        # o email não vai ser apresentavel, apenas na hora de escrever/salvar
        extra_kwargs = {
            'email': {'write_only': True}
        }
        # modelo que estara pegando os dados
        model = Avalicacao
        # campos que queremos apresentar
        fields = ('id', 'curso', 'nome', 'email', 'comentario', 'avaliacao', 'criacao', 'ativo')


class CursoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ('id', 'titulo', 'url', 'criacao', 'ativo')
