from django.db import models


class Base(models.Model):
    # data automatica do sistema
    criacao = models.DateTimeField(auto_now_add=True)
    # sempre que atualizar
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Curso(Base):
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        # qual campo sera ordenado
        ordering = ['id']
        # # decrescente
        # ordering = ['-id']

    def __str__(self):
        return self.titulo


class Avalicacao(Base):
    curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)  # 4.5

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        # pessoa com mesmo email não pode avaliar mais de uma vez o curso (email => curso)
        unique_together = ['email', 'curso']
        # qual campo sera ordenado
        ordering = ['id']

    def __str__(self):
        return f'{self.nome} avaliou o curso {self.curso}, com nota {self.avaliacao}'
