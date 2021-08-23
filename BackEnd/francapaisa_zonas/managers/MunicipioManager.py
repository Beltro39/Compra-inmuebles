from django.db import models as models

from francapaisa_zonas.querysets.MunicipioQuerySet import MunicipioQuerySet

class MunicipioManager (models.Manager):

    def get_query_set (self):

        return MunicipioQuerySet (self.model, using = self._db)

    def get_all (self):

        return self.get_query_set ().get_all ()

    def get_by_id_municipio (self, idMunicipio):

        return self.get_query_set ().get_by_id_municipio (idMunicipio)

    def get_by_nombre (self, nombre):

        return self.get_query_set ().get_by_nombre (nombre)
