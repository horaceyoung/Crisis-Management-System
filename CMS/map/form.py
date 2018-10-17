from django import forms
from map.models import LocationModel
from django_google_maps.widgets import GoogleMapsAddressWidget


class LocationForm(forms.ModelForm):

    class Meta(object):
        model = LocationModel
        fields = ['address', 'geolocation']
        widgets = {
            "address": GoogleMapsAddressWidget,
        }