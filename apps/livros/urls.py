from django.urls import path
from apps.livros.views import index,livros_lidos

urlpatterns = [
    path('', index,name='index'),
    path('livrosLidos/<int:foto_id>', livros_lidos, name='livrosLidos')
]