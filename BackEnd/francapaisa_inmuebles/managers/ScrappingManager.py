from django.db import models as models

from francapaisa_inmuebles.querysets.ScrappingQuerySet import ScrappingQuerySet

class ScrappingManager (models.Manager):

    def get_query_set (self):

        return ScrappingQuerySet (self.model, using = self._db)

    def get_all (self):

        return self.get_query_set ().get_all ()

    def get_by_id_scrapping (self, idScrapping):

        return self.get_query_set ().get_by_id_scrapping (idScrapping)
