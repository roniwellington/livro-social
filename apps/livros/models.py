from django.db import models
from datetime import datetime

class Livro(models.Model):
    
    OPCOES_CATEGORIA = [
        ("FICÇÃO CIENTÍFICA", "Ficção Científica"),
        ("FANTASIA", "Fantasia"),
        ("BIOGRAFIA", "Biografia"),
        ("NEGÓCIOS E ECONÔMIA", "Negócios e Econômia"),
        ("CIÊNCIAS", "Ciências"),
        ("OUTROS", "Outros"),
    ]
    
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    imagem = models.ImageField(upload_to="imagens/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)
    data_publicada = models.DateTimeField(default=datetime.now, blank=False)
    
    def __str__(self):
        return self.nome
    
