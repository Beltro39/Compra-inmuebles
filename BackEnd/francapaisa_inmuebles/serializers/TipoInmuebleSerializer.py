from francapaisa_inmuebles.serializers.BaseSerializer import BaseSerializer

from francapaisa_inmuebles.models.TipoInmuebleModel import TipoInmuebleModel

class TipoInmuebleSerializer (BaseSerializer):

    class Meta:

        model            = TipoInmuebleModel

        fields           = ['idTipoInmueble',
                            'nombre'] + BaseSerializer.Meta.fields

        read_only_fields = ['idTipoInmueble',
                            'nombre'] + BaseSerializer.Meta.read_only_fields
