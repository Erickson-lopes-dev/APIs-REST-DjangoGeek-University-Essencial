from django.urls import path
from .views import CursoAPIView, AvaliazaoAPIView

urlpatterns = [
    path('cursos/', CursoAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvaliazaoAPIView.as_view(), name='avaliacoes')
]