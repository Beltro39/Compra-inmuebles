from django.utils.translation import gettext_lazy as _

from django.db import models as models

from francapaisa_inmuebles.models.BaseModel import BaseModel

from francapaisa_inmuebles.managers.TipoInmuebleManager import TipoInmuebleManager

class TipoInmuebleModel (BaseModel):

    idTipoInmueble       = models.AutoField (db_column   = 'idTipoInmueble',
                                          blank       = False,
                                          null        = False,
                                          unique      = True,
                                          editable    = False,
                                          primary_key = True)

    nombre            = models.CharField (db_column  = 'nombre',
                                          max_length = 50,
                                          blank      = False,
                                          null       = False)

    objects = TipoInmuebleManager ()

    def __str__ (self):

        return "{0} ({1})".format (self.idTipoInmueble,
                                   self.nombre)

    class Meta:

        app_label = 'francapaisa_inmuebles'

        db_table = 'TipoInmueble'
        ordering = ['nombre', 'idTipoInmueble']
