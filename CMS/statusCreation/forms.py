from django import forms
from models import Incident
class UpdateForm(forms.ModelForm):

    status = forms.CharField()

    class Meta:
        model = Incident
        fields = ('incident_status',)