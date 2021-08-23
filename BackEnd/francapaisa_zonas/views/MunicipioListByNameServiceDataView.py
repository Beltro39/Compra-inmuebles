from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from oauth2_provider.contrib.rest_framework import TokenHasScope

from francapaisa_zonas.models.MunicipioModel import MunicipioModel

from francapaisa_zonas.serializers.MunicipioSerializer import MunicipioSerializer

class MunicipioListByNameServiceDataView (APIView):

#    authentication_classes = [OAuth2Authentication]
#    permission_classes     = [TokenHasScope]
#    required_scopes        = ['francapaisa_zonas_scope']

    @method_decorator(csrf_exempt)
    def get (self, request, nombre, format = None, *args, **kwargs):

        municipioData = MunicipioModel.objects.get_by_nombre (nombre)

        municipioSerializer = MunicipioSerializer (municipioData,
                                                   many = True)

        return Response (municipioSerializer.data)
