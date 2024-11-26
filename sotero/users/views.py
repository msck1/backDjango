from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuarios
from .forms import UsuarioForm, LoginForm

# Create your views here.


def listar_usuarios(request):
    if 'usuario_logado' not in request.session:
        return redirect('login')
    
    usuarios = Usuarios.objects.all()
    return render(request, 'listar.html', {'usuarios': usuarios})

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'cadastrar.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            
            try:
                usuario = Usuarios.objects.get(email=email)
                if usuario.senha == senha:
                    # Login bem-sucedido
                    request.session['usuario_logado'] = usuario.id
                    return redirect('listar_usuarios')
                else:
                    messages.error(request, 'Senha incorreta')
            except Usuarios.DoesNotExist:
                messages.error(request, 'Usuário não encontrado')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    if 'usuario_logado' in request.session:
        del request.session['usuario_logado']
    return redirect('login')