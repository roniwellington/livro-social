from django.urls import path
from livros.views import index,livros_lidos

urlpatterns = [
    path('', index),
    path('livrosLidos/', livros_lidos)
]