from django.utils.translation import gettext_lazy as _

from django.db import models as models

import django.utils.timezone

class BaseModel (models.Model):

    validStateList = (('A', _('ActiveValidStateName')),
                      ('P', _('TestValidStateName')),
                      ('I', _('InactiveValidStateName')))

    class Meta:

        abstract = True
