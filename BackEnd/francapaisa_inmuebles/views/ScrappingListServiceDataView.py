from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from oauth2_provider.contrib.rest_framework import TokenHasScope

from francapaisa_inmuebles.models.ScrappingModel import ScrappingModel

from francapaisa_inmuebles.serializers.ScrappingSerializer import ScrappingSerializer

class ScrappingListServiceDataView (APIView):

#    authentication_classes = [OAuth2Authentication]
#    permission_classes     = [TokenHasScope]
#    required_scopes        = ['francapaisa_inmuebles_scope']

    @method_decorator(csrf_exempt)
    def get (self, request, format = None, *args, **kwargs):

        scrappingData = ScrappingModel.objects.get_all ()[:60]

        scrappingSerializer = ScrappingSerializer (scrappingData,
                                                   many = True)

        return Response (scrappingSerializer.data)
