from francapaisa_zonas.serializers.BaseSerializer import BaseSerializer

from francapaisa_zonas.models.MunicipioModel import MunicipioModel

class MunicipioSerializer (BaseSerializer):

    class Meta:

        model            = MunicipioModel

        fields           = ['idMunicipio',
                            'nombre'] + BaseSerializer.Meta.fields

        read_only_fields = ['idMunicipio',
                            'nombre'] + BaseSerializer.Meta.read_only_fields
