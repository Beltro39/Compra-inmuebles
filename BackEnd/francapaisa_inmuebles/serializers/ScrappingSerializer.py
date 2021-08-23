from francapaisa_inmuebles.serializers.BaseSerializer import BaseSerializer

from francapaisa_inmuebles.models.ScrappingModel import ScrappingModel

from francapaisa_inmuebles.serializers.TipoInmuebleSerializer import TipoInmuebleSerializer
from francapaisa_zonas.serializers.MunicipioSerializer import MunicipioSerializer
from francapaisa_zonas.serializers.BarrioMedellinSerializer import BarrioMedellinSerializer

class ScrappingSerializer (BaseSerializer):

    tipo_inmueble_data = TipoInmuebleSerializer (source = 'tipo_inmueble', required = False)
    municipio_data     = MunicipioSerializer (source = 'municipio', required = False)
    barrio_data        = BarrioMedellinSerializer (source = 'barrio', required = False)

    class Meta:

        model            = ScrappingModel

        fields           = ['idScrapping','nombre_fuente', 'nombre_publicacion', 'url_fuente', 'tipo_inmueble',
                            'valor_inmueble', 'municipio', 'barrio', 'cantidad_habitaciones', 'area_total',
                            'area_construida', 'descripcion', 'vendedor', 'cantidad_banos', 'costo_administracion',
                            'cantidad_parqueaderos', 'costo_servicios_publicos', 'inmueble_nuevo', 'imagen_inmueble',
                            'fecha_ultima_modificacion', 'tipo_inmueble_data', 'municipio_data', 'barrio_data'] + BaseSerializer.Meta.fields

        read_only_fields = ['idScrapping','nombre_fuente', 'nombre_publicacion', 'url_fuente', 'tipo_inmueble',
                            'valor_inmueble', 'municipio', 'barrio', 'cantidad_habitaciones', 'area_total',
                            'area_construida', 'descripcion', 'vendedor', 'cantidad_banos', 'costo_administracion',
                            'cantidad_parqueaderos', 'costo_servicios_publicos', 'inmueble_nuevo', 'imagen_inmueble',
                            'fecha_ultima_modificacion', 'tipo_inmueble_data', 'municipio_data', 'barrio_data'] + BaseSerializer.Meta.read_only_fields
