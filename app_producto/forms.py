from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio_venta', 'stock', 'id_marca', 'id_famillia']
        labels = {
            'nombre': 'Nombre',
            'precio_venta': 'Precio de Venta',
            'stock': 'Stock',
            'id_marca': 'ID Marca',
            'id_famillia': 'ID Familia',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_venta': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_marca': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_famillia': forms.NumberInput(attrs={'class': 'form-control'}),
        }
