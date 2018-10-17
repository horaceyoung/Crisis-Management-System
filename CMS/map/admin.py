from django.contrib import admin
from django.db import models
# Register your models here.
from mapwidgets.widgets import GooglePointFieldWidget


class CityAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }