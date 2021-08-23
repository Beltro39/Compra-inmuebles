from django.utils.translation import gettext_lazy as _

from django.db import models as models

from francapaisa_zonas.models.BaseModel import BaseModel

from francapaisa_zonas.managers.MunicipioManager import MunicipioManager

class MunicipioModel (BaseModel):

    idMunicipio       = models.AutoField (db_column   = 'idMunicipio',
                                          blank       = False,
                                          null        = False,
                                          unique      = True,
                                          editable    = False,
                                          primary_key = True)

    nombre            = models.CharField (db_column  = 'nombre',
                                          max_length = 50,
                                          blank      = False,
                                          null       = False)

    objects = MunicipioManager ()

    def __str__ (self):

        return "{0} ({1})".format (self.idMunicipio,
                                   self.nombre)

    class Meta:

        app_label = 'francapaisa_zonas'

        db_table = 'Municipio'
        ordering = ['nombre', 'idMunicipio']
