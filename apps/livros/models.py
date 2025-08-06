from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Livro(models.Model):
    
    OPCOES_CATEGORIA = [
        ("FICÇÃO CIENTÍFICA", "Ficção Científica"),
        ("FANTASIA", "Fantasia"),
        ("BIOGRAFIA", "Biografia"),
        ("NEGÓCIOS E ECONÔMIA", "Negócios e Econômia"),
        ("CIÊNCIAS", "Ciências"),
        ("AVENTURA", "Aventura"),
        ("OUTROS", "Outros"),
    ]
    
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    imagem = models.ImageField(upload_to="imagens/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=True)
    data_publicada = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )
    
    def __str__(self):
        return self.nome
    
