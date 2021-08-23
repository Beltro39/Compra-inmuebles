from django.db import models as models

from django.apps import apps

from django.conf import settings

class TipoInmuebleQuerySet (models.query.QuerySet):

    def get_all (self):

        return self

    def get_by_id_tipo_inmueble (self, idTipoInmueble):

        return self.filter (idTipoInmueble = idTipoInmueble)
