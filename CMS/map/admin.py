from django.contrib import admin
<<<<<<< HEAD
from django.db import models
# Register your models here.
from mapwidgets.widgets import GooglePointFieldWidget


class CityAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
=======
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
>>>>>>> 80e9cda4286f94a0c995bc660210e02980d9a91c
    }