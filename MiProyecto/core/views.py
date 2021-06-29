from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'core/index.html')


def contacto(request):
    return render(request,'core/contacto.html')


def login(request):
    return render(request, 'core/login.html')


def artista(request):
    return render(request, 'core/artista.html')


def categoria(request):
    return render(request, 'core/categoria.html')

def formulario(request):
    return render(request, 'core/formulario.html')

def listap(request):
    return render(request, 'core/listap.html')

def recuperar(request):
    return render(request, 'core/recuperar.html')

def registro(request):
    return render(request, 'core/registro.html')

def compraVenta(request):
    return render(request, 'core/compraVenta.html')


