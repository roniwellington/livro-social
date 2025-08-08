from django import forms
from apps.livros.models import Livro

class LivroForms(forms.ModelForm):
    class Meta:
        model = Livro
        exclude = ['publicada',]
        labels = {
            'descricao': 'Descrição',
            'data_publicada': 'Data de registro',
            'usuario': 'Usuário'
        }
        
        widgets = {
            'nome':forms.TextInput(attrs={'class':'input-field'}),
            'legenda':forms.TextInput(attrs={'class':'input-field'}),
            'categoria':forms.Select(attrs={'class':'input-field'}),
            'descricao':forms.Textarea(attrs={'class':'input-field'}),
            'imagem':forms.FileInput(attrs={'class':'input-field'}),
            'data_publicada':forms.DateInput(
                format= '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'input-field'}
                ),
            'usuario':forms.Select(attrs={'class':'input-field'}),
        }
        