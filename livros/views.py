from django.shortcuts import render, get_object_or_404
from livros.models import Livro



def index(request):
    livros = Livro.objects.order_by("data_publicada").filter(publicada=True)
    return render(request, 'livros/index.html', {"cards": livros})

def livros_lidos(request, foto_id):
    livro_Id = get_object_or_404(Livro, pk=foto_id)
    return render(request, 'livros/livrosLidos.html', {"livro":livro_Id})
    

# Create your views here.
