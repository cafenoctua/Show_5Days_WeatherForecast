from django import forms
from .load_citynames import load_citynames

from .models import InputCity

class InputCityForm(forms.ModelForm):
    
    class Meta:
        model = InputCity
        fields = ('input_city_name',\
        )

        widgets = {
            'input_city_name': forms.TextInput(attrs={'size': 10}),
        }