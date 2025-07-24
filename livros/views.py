from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'livros/index.html')

def livros_lidos(request):
    return render(request, 'livros/livrosLidos.html')
    

# Create your views here.
