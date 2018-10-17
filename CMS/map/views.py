from django.shortcuts import render
from django.views.generic import FormView

from map.form import LocationForm

class LocationFormView(FormView):
    form_class = LocationForm
    template_name = "map/map_home.html"