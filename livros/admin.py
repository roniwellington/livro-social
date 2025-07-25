from django.contrib import admin
from livros.models import Livro

class ListandoLivros(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "descricao", "imagem")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)

admin.site.register(Livro, ListandoLivros)
