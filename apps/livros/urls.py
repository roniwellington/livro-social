from django.urls import path
from apps.livros.views import index,livros_lidos, novo_livro, editar_livro, deletar_livro, filtro

urlpatterns = [
    path('', index,name='index'),
    path('livrosLidos/<int:foto_id>', livros_lidos, name='livrosLidos'),
    path('novo-livro', novo_livro, name='novo_livro'),
    path('editar-livro/<int:livro_id>', editar_livro, name='editar_livro'),
    path('deletar-livro/<int:livro_id>', deletar_livro, name='deletar_livro'),
    path('filtro/<str:categoria>', filtro, name='filtro'),
]