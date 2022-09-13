from django.db import models
from django.utils.translation import gettext as _



class Widget(models.Model):
    Title = models.fields.CharField(_("intitule_formation"), max_length=10000)
    Temps = models.fields.CharField(_("nombre_heures_total_max"),max_length=1000)
    Prix = models.fields.CharField(_("frais_ttc_tot_max"),max_length=100)
    Option = models.fields.CharField(_("nom_departement"),max_length=100)








