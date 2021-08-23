"""francapaisa_inmuebles URL Configuration

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

from francapaisa_inmuebles.views.TipoInmuebleListServiceDataView import TipoInmuebleListServiceDataView
from francapaisa_inmuebles.views.TipoInmuebleListByIdServiceDataView import TipoInmuebleListByIdServiceDataView
from francapaisa_inmuebles.views.ScrappingListServiceDataView import ScrappingListServiceDataView
from francapaisa_inmuebles.views.ScrappingListByIdServiceDataView import ScrappingListByIdServiceDataView

urlpatterns = []

francapaisa_inmuebles_endpoint_views = [
                                       path    ('tipo-inmueble/<int:idTipoInmueble>/',
                                                TipoInmuebleListByIdServiceDataView.as_view (),
                                                name = "tipo-inmueble-list-by-id"),

                                       path    ('tipo-inmueble/',
                                                TipoInmuebleListServiceDataView.as_view (),
                                                name = "tipo-inmueble"),

                                       path    ('scrapping/<int:idScrapping>/',
                                                ScrappingListByIdServiceDataView.as_view (),
                                                name = "scrapping-list-by-id"),

                                       path    ('scrapping/',
                                                ScrappingListServiceDataView.as_view (),
                                                name = "scrapping"),
                                   ]

urlpatterns += francapaisa_inmuebles_endpoint_views
