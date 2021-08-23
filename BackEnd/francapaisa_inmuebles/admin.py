from django.contrib import admin

# Register your models here.

# Data from PerfilUsuarioCCV2 should be displayed in the admin site           #

from francapaisa_inmuebles.models.TipoInmuebleModel import TipoInmuebleModel
from francapaisa_inmuebles.models.ScrappingModel import ScrappingModel

from francapaisa_inmuebles.admins.TipoInmuebleAdmin import TipoInmuebleAdmin
from francapaisa_inmuebles.admins.ScrappingAdmin import ScrappingAdmin

admin.site.register (TipoInmuebleModel, TipoInmuebleAdmin)
admin.site.register (ScrappingModel, ScrappingAdmin)
