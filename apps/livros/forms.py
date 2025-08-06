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
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'legenda':forms.TextInput(attrs={'class':'form-control'}),
            'categoria':forms.Select(attrs={'class':'form-control'}),
            'descricao':forms.Textarea(attrs={'class':'form-control'}),
            'imagem':forms.FileInput(attrs={'class':'form-control'}),
            'data_publicada':forms.DateInput(
                format= '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'}
                ),
            'usuario':forms.Select(attrs={'class':'form-control'}),
        }
        