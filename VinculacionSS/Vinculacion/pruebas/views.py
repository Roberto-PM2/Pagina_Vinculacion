from django.shortcuts import render

# Create your views here.

def mensaje(request):
    return render(request, 'mensaje.html')

def servicio(request):
    return render(request, 'ServicioSocial.html')


def inicio(request):
    return render(request, 'MainPage.html')


def bolsatrabajo(request):
    return render(request, 'BolsaTrabajo.html')


def seguridad(request):
    return render(request, 'Seguridad.html')


def eb(request):
    return render(request, 'eb.html')

def area(request):
    return render(request, 'AreaAdministrativa.html')

def fortalecimiento(request):
    return render(request, 'fortalecimiento.html')