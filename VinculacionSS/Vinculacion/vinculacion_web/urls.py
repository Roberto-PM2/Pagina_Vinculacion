from django.urls import path
from vinculacion_web import views


urlpatterns = [
    path('servicio/', views.servicio, name='servicio'),
    path('hola/', views.mensaje),
    path('inicio/', views.inicio, name='inicio'),  # Agregamos la URL para la vista 'inicio'
    path('sector_productivo/', views.sector_productivo, name='sector_productivo'),  # Agregamos la URL para la vista 'bolsatrabajo'
    path('estudios_factibilidad/', views.estudios_factibilidad, name='estudios_factibilidad'),  # Agregamos la URL para la vista 'seguridad'
    path('educacion_continua/', views.educacion_continua, name='educacion_continua'),  # Agregamos la URL para la vista 'eb'
    path('area_administrativa/', views.area_administrativa, name='area_administrativa'),  # Agregamos la URL para la vista 'area'
    path('fortalecimiento/', views.fortalecimiento, name='fortalecimiento'),  # Agregamos la URL para la vista 'fortalecimiento'
    path('certificacion/', views.certificacion, name='certificacion'),
]
