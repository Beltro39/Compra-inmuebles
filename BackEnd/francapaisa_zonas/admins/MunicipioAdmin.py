from django.contrib import admin

class MunicipioAdmin (admin.ModelAdmin):

    list_display  = ["idMunicipio", "nombre"]

    search_fields = ["idMunicipio", "nombre"]

    list_filter   = ["idMunicipio", "nombre"]

    ordering      = ["nombre"]
