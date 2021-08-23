from django.contrib import admin

class BarrioMedellinAdmin (admin.ModelAdmin):

    list_display  = ["idBarrioMedellin", "nombre"]

    search_fields = ["idBarrioMedellin", "nombre"]

    list_filter   = ["idBarrioMedellin", "nombre"]

    ordering      = ["nombre"]
