from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def compras(request):
    return render(request, 'compras.html')

def inise(request):
    return render(request, 'inise.html')

def registrar(request):
    return render(request, 'registrar.html')