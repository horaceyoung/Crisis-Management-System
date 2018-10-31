from django import forms

class StatusForm(forms.Form):
    post = forms.CharField()
