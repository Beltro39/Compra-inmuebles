from django.db import models as models

from francapaisa_zonas.querysets.BarrioMedellinQuerySet import BarrioMedellinQuerySet

class BarrioMedellinManager (models.Manager):

    def get_query_set (self):

        return BarrioMedellinQuerySet (self.model, using = self._db)

    def get_all (self):

        return self.get_query_set ().get_all ()

    def get_by_id_barrio_medellin (self, idBarrioMedellin):

        return self.get_query_set ().get_by_id_barrio_medellin (idBarrioMedellin)

    def get_by_nombre (self, nombre):

        return self.get_query_set ().get_by_nombre (nombre)
