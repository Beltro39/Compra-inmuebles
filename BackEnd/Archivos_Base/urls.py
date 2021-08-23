"""Archivos_Base URL Configuration

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

from django.urls import include, path, re_path

from django.conf import settings

from django.contrib import admin
import oauth2_provider.views as oauth2_views

urlpatterns = []

# Django OAuth Toolkit OAuth2 Provider Endpoints

dot_oauth2_endpoint_views = [
                                re_path (r'^authorize/$',
                                         oauth2_views.AuthorizationView.as_view (),
                                         name = "authorize"),

                                re_path (r'^token/$',
                                         oauth2_views.TokenView.as_view (),
                                         name = "token"),

                                re_path (r'^revoke-token/$',
                                         oauth2_views.RevokeTokenView.as_view (),
                                         name = "revoke-token"),

                                re_path (r'^introspect/$',
                                         oauth2_views.IntrospectTokenView.as_view (),
                                         name = "instrospect"),
                            ]

if settings.DEBUG:

    # Django OAuth Toolkit OAuth2 Application Management Endpoints

    dot_oauth2_endpoint_views += [
                                     re_path (r'^applications/$',
                                              oauth2_views.ApplicationList.as_view (),
                                              name = "list"),

                                     re_path (r'^applications/register/$',
                                              oauth2_views.ApplicationRegistration.as_view (),
                                              name = "register"),

                                     re_path (r'^applications/(?P<pk>\d+)/$',
                                              oauth2_views.ApplicationDetail.as_view (),
                                              name = "detail"),

                                     re_path (r'^applications/(?P<pk>\d+)/delete/$',
                                              oauth2_views.ApplicationDelete.as_view (),
                                              name = "delete"),

                                     re_path (r'^applications/(?P<pk>\d+)/update/$',
                                              oauth2_views.ApplicationUpdate.as_view (),
                                              name = "update"),
                                 ]

    # Django OAuth Toolkit  OAuth2 Token Management Endpoints

    dot_oauth2_endpoint_views += [
                                     re_path (r'^authorized-tokens/$',
                                              oauth2_views.AuthorizedTokensListView.as_view() ,
                                              name = "authorized-token-list"),

                                     re_path (r'^authorized-tokens/(?P<pk>\d+)/delete/$',
                                              oauth2_views.AuthorizedTokenDeleteView.as_view(),
                                              name = "authorized-token-delete"),
                                 ]

    # Django Admin Application Management Endpoints
    urlpatterns += [
                       re_path (r'^admin/', admin.site.urls),
                   ]

urlpatterns += [
                   re_path (r'^oauth/',
                            include ((dot_oauth2_endpoint_views,
                            'oauth2_provider'),
                            namespace = 'oauth2_provider')),
               ]

# francapaisa_zonas data endpoints

urlpatterns += [
                   re_path (r'^v0/francapaisa-zonas/',
                            include (('francapaisa_zonas.urls',
                            'francapaisa_zonas'),
                            namespace = 'francapaisa_zonas')),
               ]

# francapaisa_inmuebles data endpoints

urlpatterns += [
                   re_path (r'^v0/francapaisa-inmuebles/',
                            include (('francapaisa_inmuebles.urls',
                            'francapaisa_inmuebles'),
                            namespace = 'francapaisa_inmuebles')),
               ]
