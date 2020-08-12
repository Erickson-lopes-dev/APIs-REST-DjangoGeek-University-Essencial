from django.urls import path
from .views import CursoAPIView, AvaliacaoAPIView, CursosAPIView, AvaliacoesAPIView

urlpatterns = [
    # Todos os cursos
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    # Cada Curso em especifico
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
    # todas as avaliacoes de um curso
    path('cursos/<int:curso_pk>/avaliacoes', AvaliacoesAPIView.as_view(), name='curso_avaliacoes'),
    # avaliação especifica do curso
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='curso_avaliacao'),

    # todas as avaliações
    path('avaliacoes/', AvaliacaoAPIView.as_view(), name='avaliacoes'),
    # Cada Avaliação em especifico
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacoesAPIView.as_view(), name='avaliacao'),
]
