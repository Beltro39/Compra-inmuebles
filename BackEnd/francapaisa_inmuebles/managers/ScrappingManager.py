from django.db import models as models

from francapaisa_inmuebles.querysets.ScrappingQuerySet import ScrappingQuerySet


class ScrappingManager(models.Manager):

    def get_query_set(self):
        return ScrappingQuerySet(self.model, using=self._db)

    def get_all(self):
        return self.get_query_set().get_all()

    def get_by_id_scrapping(self, idScrapping):
        return self.get_query_set().get_by_id_scrapping(idScrapping)

    def get_by_id_tipo_inmueble(self, idTipoInmueble):
        return self.get_query_set().get_by_id_tipo_inmueble(idTipoInmueble)

    def get_by_valor_inmueble(self, valorInmuebleMinimo, valorInmuebleMaximo):
        return self.get_query_set().get_by_valor_inmueble(valorInmuebleMinimo, valorInmuebleMaximo)

    def get_by_area_total(self, areaTotalMinima, areaTotalMaxima):
        return self.get_query_set().get_by_area_total(areaTotalMinima, areaTotalMaxima)

    def get_by_cantidad_banos(self, cantidadBanos):
        return self.get_query_set().get_by_cantidad_banos(cantidadBanos)

    def get_by_cantidad_habitaciones(self, cantidadHabitaciones):
        return self.get_query_set().get_by_cantidad_habitaciones(cantidadHabitaciones)
