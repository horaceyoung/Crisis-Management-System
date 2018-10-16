from django.db import models
from django import forms
import sys, os


sys.path.append(os.path.abspath(os.path.join('..', 'callcentre')))

from callcentre.models import Incident


class ContactForm2(forms.ModelForm):
    class Meta:
        model=Incident                    #表明这个表单继承自叫 RemarkForm的模型
        fields=('caller_name','mobile_number','incident_time', 'incident_location', 'incident_category')           #指定表单继承模型的哪些属性