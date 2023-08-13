from django.forms import ModelForm
from django import forms
from .models import Mobile, Brand


class MobileForm(ModelForm):
    class Meta:
        model = Mobile
        fields = '__all__'
        # fields = ('brand_id', 'price', 'color',
        #           'screen_size', 'status', 'builder_country')
        labels = {
            "brand_id": 'Brand:',
            "model": "",
            "price": '',
            "color": '',
            "screen_size": '',
            "status": 'Status',
            "builder_country": '',
        }
        widgets = {
            "brand_id": forms.Select(attrs={'class': 'form-select'}),
            "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            "model": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Model'}),
            "price": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            "color": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Color'}),
            "screen_size": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Screen size'}),
            "status": forms.Select(attrs={'class': 'form-select'}),
            "builder_country": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Builder country'}),
        }


class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
        labels = {
            "name": '',
            "nationality": '',
        }
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            "nationality": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nationality'}),
        }
