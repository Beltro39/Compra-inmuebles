"""Archivos_Base URL Configuration"""

from django.contrib import admin
from django.urls import path
from BackEnd.ConsultaInmuebles import urls as ConsultaInmueblesURLS
from BackEnd.Usuarios import urls as UsuariosURLS
from BackEnd.Scrapping_Web import urls as ScrappingURLS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ConsultaInmuebles/', ConsultaInmueblesURLS),
    path('Usuarios/', UsuariosURLS),
    path('Scrapping_Web/', ScrappingURLS)
]
