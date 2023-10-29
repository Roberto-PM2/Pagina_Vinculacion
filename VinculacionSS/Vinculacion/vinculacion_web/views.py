from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

def mensaje(request):
    return render(request, 'mensaje.html')

def servicio(request):
    return render(request, 'ServicioSocial.html')


def inicio(request):
    return render(request, 'MainPage.html')


def sector_productivo(request):
    return render(request, 'SectorProductivo.html')


def estudios_factibilidad(request):
    return render(request, 'Estudios_Factibilidad.html')


def educacion_continua(request):
    return render(request, 'EducacionContinua.html')

def area_administrativa(request):
    return render(request, 'AreaAdministrativa.html')

def fortalecimiento(request):
    return render(request, 'fortalecimiento.html')