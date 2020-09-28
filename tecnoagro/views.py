from django.shortcuts import render
from django.utils import timezone
from .models import Consulta, Usuario
from django.views import generic
from .forms import Usuarioconsulta, Usuarioform
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate

# Create your views here.
def consultar(request):
   return render(request, 'consultar.html', {})

def home(request):
	return render(request, 'home_tecnoagro.html', {})

def somos(request):
	return render(request, 'quienessomos.html', {})

def aplicaciones(request):
	return render(request, 'aplicaciones.html', {})

def registro(request):
	return render(request, 'registro.html', {})
@login_required
def descargas(request):
	return render(request, 'descargas.html', {})

def consulta_usuario(request):
    data = {
        'form':Usuarioconsulta()
    }
    if request.method == 'POST':
        formularioo = Usuarioconsulta(request.POST)
        if formularioo.is_valid():
            formularioo.save()
            data['mensaje'] = "Consulta enviada "

    return render(request, 'consulta.html',data)

def login(request):
    return render(request, 'login.html', {})
	
class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')