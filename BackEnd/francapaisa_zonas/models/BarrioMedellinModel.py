from django.utils.translation import gettext_lazy as _

from django.db import models as models

from francapaisa_zonas.models.BaseModel import BaseModel

from francapaisa_zonas.managers.BarrioMedellinManager import BarrioMedellinManager

class BarrioMedellinModel (BaseModel):

    idBarrioMedellin       = models.AutoField (db_column   = 'idBarrioMedellin',
                                               blank       = False,
                                               null        = False,
                                               unique      = True,
                                               editable    = False,
                                               primary_key = True)

    nombre                 = models.CharField (db_column  = 'nombre',
                                               max_length = 50,
                                               blank      = False,
                                               null       = False)

    objects = BarrioMedellinManager ()

    def __str__ (self):

        return "{0} ({1})".format (self.idBarrioMedellin,
                                   self.nombre)

    class Meta:

        app_label = 'francapaisa_zonas'

        db_table = 'BarrioMedellin'
        ordering = ['nombre', 'idBarrioMedellin']
