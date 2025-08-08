from django.shortcuts import render, get_object_or_404, redirect
from apps.livros.models import Livro
from apps.livros.forms import LivroForms
from django.contrib import messages



def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
        
    livros = Livro.objects.order_by("data_publicada").filter(publicada=True)
    return render(request, 'livros/index.html', {"cards": livros})

def livros_lidos(request, foto_id):
    livro_Id = get_object_or_404(Livro, pk=foto_id)
    return render(request, 'livros/livrosLidos.html', {"livro":livro_Id})
    

def novo_livro(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    form = LivroForms
    if request.method == 'POST':
        form = LivroForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #messages.SUCCESS(request, 'Novo livro cadastrado!')
            return redirect('index')
        
    return render(request, 'livros/novo_livro.html', {'form': form})

def editar_livro(request, livro_id):
    livro = Livro.objects.get(id=livro_id)
    form = LivroForms(instance=livro)
    if request.method == 'POST':
        form = LivroForms(request.POST, request.FILES, instance=livro)
        if form.is_valid():
            form.save()
            #messages.SUCCESS(request, 'livro editado com sucesso')
            return redirect('index')
        
    return render(request,'livros/editar_livro.html', {'form':form, 'livro_id':livro_id})

def deletar_livro(request, livro_id):
    livro = Livro.objects.get(id=livro_id)
    livro.delete()
    messages.success(request, 'Deleção feita com sucesso!')
    return redirect('index')
