from django.urls import path
from vinculacion_web import views


urlpatterns = [
    path('servicio/', views.servicio, name='servicio'),
    path('hola/', views.mensaje),
    path('inicio/', views.inicio, name='inicio'),  # Agregamos la URL para la vista 'inicio'
    path('bolsatrabajo/', views.bolsatrabajo, name='bolsatrabajo'),  # Agregamos la URL para la vista 'bolsatrabajo'
    path('seguridad/', views.seguridad, name='seguridad'),  # Agregamos la URL para la vista 'seguridad'
    path('eb/', views.eb, name='eb'),  # Agregamos la URL para la vista 'eb'
    path('area/', views.area, name='area'),  # Agregamos la URL para la vista 'area'
    path('fortalecimiento/', views.fortalecimiento, name='fortalecimiento'),  # Agregamos la URL para la vista 'fortalecimiento'
]
