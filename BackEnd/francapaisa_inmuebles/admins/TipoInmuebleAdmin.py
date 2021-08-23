from django.contrib import admin

class TipoInmuebleAdmin (admin.ModelAdmin):

    list_display  = ["idTipoInmueble", "nombre"]

    search_fields = ["idTipoInmueble", "nombre"]

    list_filter   = ["idTipoInmueble", "nombre"]

    ordering      = ["nombre"]
