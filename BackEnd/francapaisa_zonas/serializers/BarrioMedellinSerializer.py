from francapaisa_zonas.serializers.BaseSerializer import BaseSerializer

from francapaisa_zonas.models.BarrioMedellinModel import BarrioMedellinModel

class BarrioMedellinSerializer (BaseSerializer):

    class Meta:

        model            = BarrioMedellinModel

        fields           = ['idBarrioMedellin',
                            'nombre'] + BaseSerializer.Meta.fields

        read_only_fields = ['idBarrioMedellin',
                            'nombre'] + BaseSerializer.Meta.read_only_fields
