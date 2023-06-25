from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request, 'index.html', {})

def publicaciones_view(request):
    return render(request, 'publicaciones.html', {})

def contactos_view(request):
    return render(request, 'contactos.html', {})

def registrarse_view(request):
    return render(request, 'registrarse.html', {})

def iniciar_sesion_view(request):
    return render(request, 'iniciar-sesion.html', {})

def cerrar_sesion_view(request):
    return render(request, 'cerrar-sesion.html', {})