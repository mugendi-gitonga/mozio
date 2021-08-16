from django import forms
from django.forms import ModelForm
from .models import Provider, Polygon
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm


class ProviderForm(ModelForm):
	
	class Meta:
		model = Provider
		fields = ('name', 'email','phone_number','language', 'currency')
		widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control'}),
        	'email': forms.EmailInput(attrs={'class': 'form-control'}),
			'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'language': forms.Select(attrs={'class': 'form-control'}),
            'currency': forms.Select(attrs={'class': 'form-control'})
		},


class PolygonForm(ModelForm):

    class Meta:
        model = Polygon
        fields= ('polygon_name', 'price', 'polygon_area')
        widgets = {

            'polygon_name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'polygon_area': forms.TextInput(attrs={'class': 'form-control'}),
        },


class PolygonFormUpdate(ModelForm):

    class Meta:
        model = Polygon
        fields= ('polygon_name', 'price', 'polygon_area')
        widgets = {

            'polygon_name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'polygon_area': forms.TextInput(attrs={'class': 'form-control'}),
            
        },


class GetProviderForm(forms.Form):

    lattitude = forms.FloatField()
    longitude = forms.FloatField()

