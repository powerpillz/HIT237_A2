from django import forms
from .models import *

class MineralForm(forms.ModelForm):
    class Meta:
        model = Minerals
        exclude = []

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = []

class MinesiteForm(forms.ModelForm):
    class Meta:
        model = Minesite
        exclude = []
