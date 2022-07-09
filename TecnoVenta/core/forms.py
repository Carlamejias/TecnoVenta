from django import forms
from django.forms import ModelForm
from .models import Producto

class ProductoForm(ModelForm):
     
     class Meta:
        model = Producto
        fields =['idProducto', 'marca', 'precio', 'modelo', 'categoria']
          
class FormularioContacto(forms.Form):
   
   nombre=forms.CharField()
   correo=forms.EmailField()
   rut=forms.IntegerField()
   tel=forms.IntegerField()
   ciudad=forms.CharField()
   tipo=forms.BooleanField()
   coment=forms.CharField()
