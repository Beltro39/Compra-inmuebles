from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from oauth2_provider.contrib.rest_framework import TokenHasScope

from francapaisa_inmuebles.models.ScrappingModel import ScrappingModel

from francapaisa_inmuebles.serializers.ScrappingSerializer import ScrappingSerializer

class ScrappingListByFilterServicePaginatedDataView (APIView):

#    authentication_classes = [OAuth2Authentication]
#    permission_classes     = [TokenHasScope]
#    required_scopes        = ['francapaisa_inmuebles_scope']

    @method_decorator(csrf_exempt)
    def post (self, request, format = None, *args, **kwargs):

#        print ("request.data = ")
#        print (request.data)
#        print ("request = ")
#        print (request)

        if ("tipo_inmueble" in request.data) or \
           (("valor_inmueble_min" in request.data) and ("valor_inmueble_max" in request.data)) or \
           (("area_total_min" in request.data) and ("area_total_max" in request.data)) or \
           ("cantidad_banos" in request.data) or \
           ("cantidad_habitaciones" in request.data):

            scrappingData = None

            if ("tipo_inmueble" in request.data):

                scrappingData = ScrappingModel.objects.get_by_id_tipo_inmueble (int (request.data["tipo_inmueble"]))

            if (("valor_inmueble_min" in request.data) and ("valor_inmueble_max" in request.data)):

                if (scrappingData is None):

                    scrappingData = ScrappingModel.objects.get_by_valor_inmueble (int (request.data["valor_inmueble_min"]), int (request.data["valor_inmueble_max"]))

                else:

                    scrappingData = scrappingData.get_by_valor_inmueble (int (request.data["valor_inmueble_min"]), int (request.data["valor_inmueble_max"]))

            if (("area_total_min" in request.data) and ("area_total_max" in request.data)):

                if (scrappingData is None):

                    scrappingData = ScrappingModel.objects.get_by_area_total (float (request.data["area_total_min"]), float (request.data["area_total_max"]))

                else:

                    scrappingData = scrappingData.get_by_area_total (float (request.data["area_total_min"]), float (request.data["area_total_max"]))

            if ("cantidad_banos" in request.data):

                if (scrappingData is None):

                    scrappingData = ScrappingModel.objects.get_by_cantidad_banos (int (request.data["cantidad_banos"]))

                else:

                    scrappingData = scrappingData.get_by_cantidad_banos (int (request.data["cantidad_banos"]))

            if ("cantidad_habitaciones" in request.data):

                if (scrappingData is None):

                    scrappingData = ScrappingModel.objects.get_by_cantidad_habitaciones (int (request.data["cantidad_habitaciones"]))

                else:

                    scrappingData = scrappingData.get_by_cantidad_habitaciones (int (request.data["cantidad_habitaciones"]))


            pageNumber = self.request.query_params.get ('pageNumber', 1)
            pageSize = self.request.query_params.get ('pageSize', 300)

            scrappingPaginator = Paginator (scrappingData , pageSize)

            try:

                scrappingSerializer = ScrappingSerializer (scrappingPaginator.page (pageNumber),
                                                           many = True,
                                                           context = {'request':request})

                return Response (scrappingSerializer.data)

            except (EmptyPage, ZeroDivisionError):

                scrappingSerializer = ScrappingSerializer ([],
                                                           many = True,
                                                           context = {'request':request})

                return Response (scrappingSerializer.data)

        else:

            return Response ("El servicio requiere para su filtro de datos al menos un parametro de busqueda", status = status.HTTP_400_BAD_REQUEST)

