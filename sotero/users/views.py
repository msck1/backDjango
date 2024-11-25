from django.shortcuts import render, redirect
from .models import Usuarios
from .forms import UsuarioForm

# Create your views here.


def listar_usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'listar.html', {'usuarios': usuarios})

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'cadastrar.html', {'form': form})
