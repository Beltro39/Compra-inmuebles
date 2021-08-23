from django.db import models as models

from francapaisa_inmuebles.querysets.TipoInmuebleQuerySet import TipoInmuebleQuerySet

class TipoInmuebleManager (models.Manager):

    def get_query_set (self):

        return TipoInmuebleQuerySet (self.model, using = self._db)

    def get_all (self):

        return self.get_query_set ().get_all ()

    def get_by_id_tipo_inmueble (self, idTipoInmueble):

        return self.get_query_set ().get_by_id_tipo_inmueble (idTipoInmueble)
