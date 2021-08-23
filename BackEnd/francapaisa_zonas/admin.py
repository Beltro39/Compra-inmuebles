from django.contrib import admin

# Register your models here.

# Data from PerfilUsuarioCCV2 should be displayed in the admin site           #

from francapaisa_zonas.models.MunicipioModel import MunicipioModel
from francapaisa_zonas.models.BarrioMedellinModel import BarrioMedellinModel

from francapaisa_zonas.admins.MunicipioAdmin import MunicipioAdmin
from francapaisa_zonas.admins.BarrioMedellinAdmin import BarrioMedellinAdmin

admin.site.register (MunicipioModel, MunicipioAdmin)
admin.site.register (BarrioMedellinModel, BarrioMedellinAdmin)
