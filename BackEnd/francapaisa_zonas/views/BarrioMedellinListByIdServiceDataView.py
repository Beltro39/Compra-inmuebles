from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from oauth2_provider.contrib.rest_framework import TokenHasScope

from francapaisa_zonas.models.BarrioMedellinModel import BarrioMedellinModel

from francapaisa_zonas.serializers.BarrioMedellinSerializer import BarrioMedellinSerializer

class BarrioMedellinListByIdServiceDataView (APIView):

#    authentication_classes = [OAuth2Authentication]
#    permission_classes     = [TokenHasScope]
#    required_scopes        = ['francapaisa_zonas_scope']

    @method_decorator(csrf_exempt)
    def get (self, request, idBarrioMedellin, format = None, *args, **kwargs):

        barrioMedellinData = BarrioMedellinModel.objects.get_by_id_barrio_medellin (idBarrioMedellin)

        barrioMedellinSerializer = BarrioMedellinSerializer (barrioMedellinData,
                                                             many = True)

        return Response (barrioMedellinSerializer.data)