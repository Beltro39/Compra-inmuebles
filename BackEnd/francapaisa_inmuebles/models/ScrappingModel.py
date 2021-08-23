from django.utils.translation import gettext_lazy as _

from django.db import models as models

import django.utils.timezone

from francapaisa_inmuebles.models.BaseModel import BaseModel
from francapaisa_inmuebles.models.TipoInmuebleModel import TipoInmuebleModel
from francapaisa_zonas.models.MunicipioModel import MunicipioModel
from francapaisa_zonas.models.BarrioMedellinModel import BarrioMedellinModel

from francapaisa_inmuebles.managers.ScrappingManager import ScrappingManager

class ScrappingModel (BaseModel):

    idScrapping               = models.AutoField (db_column   = 'idScrapping',
                                                  blank       = False,
                                                  null        = False,
                                                  unique      = True,
                                                  editable    = False,
                                                  primary_key = True)

    nombre_fuente             = models.CharField (db_column  = 'nombre_fuente',
                                                  max_length = 2000,
                                                  blank      = False,
                                                  null       = False)

    nombre_publicacion        = models.CharField (db_column  = 'nombre_publicacion',
                                                  max_length = 2000,
                                                  blank      = False,
                                                  null       = False)

    url_fuente                = models.CharField (db_column  = 'url_fuente',
                                                  max_length = 2000,
                                                  blank      = False,
                                                  null       = False)

    tipo_inmueble             = models.ForeignKey (TipoInmuebleModel,
                                                   on_delete = models.CASCADE,
                                                   db_column = 'tipo_inmueble',
                                                   to_field  = 'idTipoInmueble',
                                                   blank     = False,
                                                   null      = False)

    valor_inmueble            = models.BigIntegerField (db_column  = 'valor_inmueble',
                                                        blank      = False,
                                                        null       = False)

    municipio                 = models.ForeignKey (MunicipioModel,
                                                   on_delete = models.CASCADE,
                                                   db_column = 'municipio',
                                                   to_field  = 'idMunicipio',
                                                   blank     = False,
                                                   null      = False)

    barrio                    = models.ForeignKey (BarrioMedellinModel,
                                                   on_delete = models.CASCADE,
                                                   db_column = 'barrio',
                                                   to_field  = 'idBarrioMedellin',
                                                   blank     = True,
                                                   null      = True)

    cantidad_habitaciones     = models.IntegerField (db_column  = 'cantidad_habitaciones',
                                                     blank      = False,
                                                     null       = False)

    area_total                = models.FloatField (db_column  = 'area_total',
                                                   blank      = False,
                                                   null       = False)

    area_construida           = models.FloatField (db_column  = 'area_construida',
                                                   blank      = True,
                                                   null       = True)

    descripcion               = models.CharField (db_column  = 'descripcion',
                                                  max_length = 2000,
                                                  blank      = True,
                                                  null       = True)

    vendedor                  = models.CharField (db_column  = 'vendedor',
                                                  max_length = 2000,
                                                  blank      = True,
                                                  null       = True)

    cantidad_banos            = models.IntegerField (db_column  = 'cantidad_banos',
                                                     blank      = False,
                                                     null       = False)

    costo_administracion      = models.BigIntegerField (db_column  = 'costo_administracion',
                                                        blank      = True,
                                                        null       = True)

    cantidad_parqueaderos     = models.IntegerField (db_column  = 'cantidad_parqueaderos',
                                                     blank      = True,
                                                     null       = True)

    costo_servicios_publicos  = models.BigIntegerField (db_column  = 'costo_servicios_publicos',
                                                        blank      = True,
                                                        null       = True)

    inmueble_nuevo            = models.BooleanField (db_column  = 'inmueble_nuevo',
                                                     default    = False,
                                                     blank      = False,
                                                     null       = False)

    imagen_inmueble           = models.CharField (db_column  = 'imagen_inmueble',
                                                  max_length = 2000,
                                                  blank      = False,
                                                  null       = False)

    fecha_ultima_modificacion = models.DateTimeField (db_column = 'fecha_ultima_modificacion',
                                                      blank     = False,
                                                      null      = False,
                                                      default   = django.utils.timezone.now)


    objects = ScrappingManager ()

    def __str__ (self):

        return "{0} ({1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19})".format (
                   self.idScrapping,
                   self.nombre_fuente,
                   self.nombre_publicacion,
                   self.url_fuente,
                   self.tipo_inmueble,
                   self.valor_inmueble,
                   self.municipio,
                   self.barrio,
                   self.cantidad_habitaciones,
                   self.area_total,
                   self.area_construida,
                   self.descripcion,
                   self.vendedor,
                   self.cantidad_banos,
                   self.costo_administracion,
                   self.cantidad_parqueaderos,
                   self.costo_servicios_publicos,
                   self.inmueble_nuevo,
                   self.imagen_inmueble,
                   self.fecha_ultima_modificacion
               )

    class Meta:

        app_label = 'francapaisa_inmuebles'

        db_table = 'TipoScrapping'
        ordering = ['municipio', 'barrio', 'tipo_inmueble', 'vendedor', 'valor_inmueble', 'nombre_fuente']
