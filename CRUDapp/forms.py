from dataclasses import field
from django.forms import ModelForm
from CRUDapp.models import Produtc

class productFrom(ModelForm):
  class Meta:
    model = Produtc
    fields = ['name_product' , 'value_product' , 'invetory_product']
