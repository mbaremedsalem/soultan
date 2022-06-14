from django import forms

from .models import Order,Product

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product','name','lastname','email','phone','city','description']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','price','image',]