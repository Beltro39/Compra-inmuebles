from django.contrib import admin

class ScrappingAdmin (admin.ModelAdmin):

    list_display  = ["idScrapping", "nombre_fuente", "nombre_publicacion", "url_fuente", "tipo_inmueble",
                     "valor_inmueble", "municipio", "barrio", "cantidad_habitaciones", "area_total",
                     "area_construida", "descripcion", "vendedor", "cantidad_banos", "costo_administracion",
                     "cantidad_parqueaderos", "costo_servicios_publicos", "inmueble_nuevo", "imagen_inmueble",
                     "fecha_ultima_modificacion"]

    search_fields = ["idScrapping", "nombre_fuente", "nombre_publicacion", "url_fuente", "tipo_inmueble",
                     "valor_inmueble", "municipio", "barrio", "cantidad_habitaciones", "area_total",
                     "area_construida", "descripcion", "vendedor", "cantidad_banos", "costo_administracion",
                     "cantidad_parqueaderos", "costo_servicios_publicos", "inmueble_nuevo", "imagen_inmueble",
                     "fecha_ultima_modificacion"]

    list_filter   = ["idScrapping", "nombre_fuente", "nombre_publicacion", "url_fuente", "tipo_inmueble",
                     "valor_inmueble", "municipio", "barrio", "cantidad_habitaciones", "area_total",
                     "area_construida", "descripcion", "vendedor", "cantidad_banos", "costo_administracion",
                     "cantidad_parqueaderos", "costo_servicios_publicos", "inmueble_nuevo", "imagen_inmueble",
                     "fecha_ultima_modificacion"]

    ordering      = ["municipio", "barrio", "tipo_inmueble", "vendedor", "valor_inmueble", "nombre_fuente"]
