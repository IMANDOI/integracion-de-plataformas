from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import ClienteForm
from django.contrib import messages
from .models import Cliente, Bodeguero, Contador
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm




def index(request):
    return render(request, 'index.html')


from django.contrib.auth.forms import AuthenticationForm

def inise(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Inicio de sesión exitoso.')
                return redirect('index')  # Redirecciona a la página de inicio
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Nombre de usuario o contraseña inválidos.')
    else:
        form = AuthenticationForm()
    list(messages.get_messages(request))
    return render(request, 'inise.html', {'form': form})


def compras(request):
    return render(request, 'compras.html')


from django.contrib.auth.models import User
from .models import Cliente
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def formularioRegistro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            try:
                form.save()  # Esto creará tanto el User como el Cliente
                
                return redirect('inise')  # Asegúrate de que 'index' es la URL a la que quieres redirigir.
            except Exception as e:
                messages.error(request, f'Error al crear la cuenta: {e}')
        else:
            messages.error(request, 'Por favor corrija los errores en el formulario.')
    else:
        form = ClienteForm()
    return render(request, 'formularioRegistro.html', {'form': form})


def vista_bod(request):
    return render(request, 'vista_bod.html')
