from django import forms
from .models import Person
from random import randint

class RideForm(forms.Form):
    searchoc = forms.CharField(label='first_name', max_length=64, required=False)
    #searchpk = forms.IntegerField(label='pk', required=False)
    # searchdc = forms.CharField(label='Search destination city', max_length=64, required=False)

class NewRideForm(forms.ModelForm):
  class Meta:
    model = Person
    exclude = []
