from django.shortcuts import render
from django.views.generic import FormView
from map.form import LocationForm
from .models import Test
from django.core.serializers.json import DjangoJSONEncoder
import json


class LocationFormView(FormView):
    form_class = LocationForm
    template_name = "map/map_home.html"

    def get_context_data(self, **kwargs):
        context = super(LocationFormView, self).get_context_data(**kwargs)
        locations = Test.objects.all()
        #locations_json = json.dumps(list(locations), cls=DjangoJSONEncoder)
        context['locations'] = locations
        return context
