"""francapaisa_zonas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path, re_path

from francapaisa_zonas.views.MunicipioListServiceDataView import MunicipioListServiceDataView
from francapaisa_zonas.views.MunicipioListByIdServiceDataView import MunicipioListByIdServiceDataView
from francapaisa_zonas.views.MunicipioListByNameServiceDataView import MunicipioListByNameServiceDataView
from francapaisa_zonas.views.BarrioMedellinListServiceDataView import BarrioMedellinListServiceDataView
from francapaisa_zonas.views.BarrioMedellinListByIdServiceDataView import BarrioMedellinListByIdServiceDataView
from francapaisa_zonas.views.BarrioMedellinListByNameServiceDataView import BarrioMedellinListByNameServiceDataView

urlpatterns = []

francapaisa_zonas_endpoint_views = [
                                       path    ('municipio/<int:idMunicipio>/',
                                                MunicipioListByIdServiceDataView.as_view (),
                                                name = "municipio-list-by-id"),

                                       path    ('municipio/<str:nombre>/',
                                                MunicipioListByNameServiceDataView.as_view (),
                                                name = "municipio-list-by-name"),

                                       path    ('municipio/',
                                                MunicipioListServiceDataView.as_view (),
                                                name = "municipio"),

                                       path    ('barrio-medellin/<int:idBarrioMedellin>/',
                                                BarrioMedellinListByIdServiceDataView.as_view (),
                                                name = "barrio-medellin-list-by-id"),

                                       path    ('barrio-medellin/<str:nombre>/',
                                                BarrioMedellinListByNameServiceDataView.as_view (),
                                                name = "barrio-medellin-list-by-name"),

                                       path    ('barrio-medellin/',
                                                BarrioMedellinListServiceDataView.as_view (),
                                                name = "barrio-medellin"),

                                   ]

urlpatterns += francapaisa_zonas_endpoint_views
