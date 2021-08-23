from django.db import models as models

from django.apps import apps

from django.conf import settings

class MunicipioQuerySet (models.query.QuerySet):

    def get_all (self):

        return self

    def get_by_id_municipio (self, idMunicipio):

        return self.filter (idMunicipio = idMunicipio)

    def get_by_nombre (self, nombre):

        return self.filter (nombre = nombre)
