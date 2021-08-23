from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from oauth2_provider.contrib.rest_framework import TokenHasScope

from francapaisa_inmuebles.models.TipoInmuebleModel import TipoInmuebleModel

from francapaisa_inmuebles.serializers.TipoInmuebleSerializer import TipoInmuebleSerializer

class TipoInmuebleListServiceDataView (APIView):

#    authentication_classes = [OAuth2Authentication]
#    permission_classes     = [TokenHasScope]
#    required_scopes        = ['francapaisa_inmuebles_scope']

    @method_decorator(csrf_exempt)
    def get (self, request, format = None, *args, **kwargs):

        tipoInmuebleData = TipoInmuebleModel.objects.get_all ()

        tipoInmuebleSerializer = TipoInmuebleSerializer (tipoInmuebleData,
                                                         many = True)

        return Response (tipoInmuebleSerializer.data)
