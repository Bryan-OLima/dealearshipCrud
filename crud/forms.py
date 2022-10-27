from django.forms import ModelForm
from crud.models import Cars

class CarsForm(ModelForm):
    class Meta:
        model = Cars
        fields = ['brand', 'model', 'year', 'color', 'price']
