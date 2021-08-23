from django.db import models as models

from django.apps import apps

from django.conf import settings

class ScrappingQuerySet (models.query.QuerySet):

    def get_all (self):

        return self

    def get_by_id_scrapping (self, idScrapping):

        return self.filter (idScrapping = idScrapping)
