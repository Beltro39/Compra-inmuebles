from django.db import models as models

from django.apps import apps

from django.conf import settings

class ScrappingQuerySet (models.query.QuerySet):

    def get_all (self):

        return self

    def get_by_id_scrapping (self, idScrapping):

        return self.filter (idScrapping = idScrapping)

    def get_by_id_tipo_inmueble (self, idTipoInmueble):

        return self.filter (tipo_inmueble = idTipoInmueble)

    def get_by_valor_inmueble (self, valorInmuebleMinimo, valorInmuebleMaximo):

        return self.filter (valor_inmueble__gte = valorInmuebleMinimo).filter (valor_inmueble__lte = valorInmuebleMaximo)

    def get_by_area_total (self, areaTotalMinima, areaTotalMaxima):

        return self.filter (area_total__gte = areaTotalMinima).filter (area_total__lte = areaTotalMaxima)

    def get_by_cantidad_banos (self, cantidadBanos):

        return self.filter (cantidad_banos__gte = cantidadBanos)

    def get_by_cantidad_habitaciones (self, cantidadHabitaciones):

        return self.filter (cantidad_habitaciones__gte = cantidadHabitaciones)


