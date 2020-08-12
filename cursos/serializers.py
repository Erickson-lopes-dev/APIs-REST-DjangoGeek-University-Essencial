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
    # --- para poucos itens
    # relacionando para inserir no get do cursos
    # varias avaliações e só leitura
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # --- para muitos itens
    # relacionando com os cursos no json colocando um link
    # avaliacoes = serializers.HyperlinkedRelatedField(
    #     # de muitos para muitos
    #     many=True,
    #     # somente leitura
    #     read_only=True,
    #     # nome da rota - ver os detalhes
    #     view_name='curso-detail')

    # para exibir o id
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = ('id', 'titulo', 'url', 'criacao', 'ativo',
                  # aqui será acrescentado o conteúdo da variavel (AvaliacaoSerializer(many=True, read_only=True))
                  'avaliacoes')
