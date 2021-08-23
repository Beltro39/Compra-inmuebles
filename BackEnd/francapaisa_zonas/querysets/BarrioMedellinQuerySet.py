from django.db import models as models

from django.apps import apps

from django.conf import settings

class BarrioMedellinQuerySet (models.query.QuerySet):

    def get_all (self):

        return self

    def get_by_id_barrio_medellin (self, idBarrioMedellin):

        return self.filter (idBarrioMedellin = idBarrioMedellin)

    def get_by_nombre (self, nombre):

        return self.filter (nombre = nombre)
