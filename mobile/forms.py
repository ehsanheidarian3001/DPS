from django.forms import ModelForm
from .models import Mobile


class MobileForm(ModelForm):
    class Meta:
        model = Mobile
        fields = '__all__'
        # fields = ('brand_id', 'price', 'color',
        #           'screen_size', 'status', 'builder_country')
