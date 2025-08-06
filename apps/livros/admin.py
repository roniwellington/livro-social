from django.contrib import admin
from apps.livros.models import Livro

class ListandoLivros(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "descricao", "imagem", "publicada")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_editable = ("publicada",)
    list_per_page = 10

admin.site.register(Livro, ListandoLivros)
