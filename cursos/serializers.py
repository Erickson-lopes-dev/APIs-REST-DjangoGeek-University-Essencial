from rest_framework import serializers
from .models import Curso, Avalicacao
from django.db.models import Avg

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

    # padrao validate + _ +nome do campo
    def validate_avaliacao(self, valor):
        if valor in range(1, 6):  # 1, 2, 3, 4, 5
            return valor
        # retorna esse erro caso o valor não corresponda
        raise serializers.ValidationError('A avaliação precisa ser um inteiro entre 1 e 5')


class CursoSerializers(serializers.ModelSerializer):
    # --- para poucos itens
    # relacionando para inserir no get do cursos
    # varias avaliações e só leitura
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # --- para muitos itens
    # relacionando com os cursos no json colocando um link
    avaliacoes = serializers.HyperlinkedRelatedField(
        # de muitos para muitos
        many=True,
        # somente leitura
        read_only=True,
        # nome da rota - ver os detalhes
        view_name='curso-detail')

    # campo que o método irá alterar ele
    media_avaliacoes = serializers.SerializerMethodField()

    # para exibir o id
    # avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = ('id', 'titulo', 'url', 'criacao', 'ativo',
                  # aqui será acrescentado o conteúdo da variavel (AvaliacaoSerializer(many=True, read_only=True))
                  'avaliacoes', 'media_avaliacoes')

        # padrao para methodfild get_nomea-tributo
        def get_media_avaliacoes(self, obj):
            media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

            # se não obter nenhuma média retorna 0
            if media is None:
                return 0

            # se encontrar media arrondonda e divide por 2
            return round(media * 2) / 2