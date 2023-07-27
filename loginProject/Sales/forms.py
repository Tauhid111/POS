from django import forms
from adminLoginApp.models import Product
from .models import Order, OrderItem

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'subtotal']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subtotal'].widget.attrs['readonly'] = True
    
    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get('product')
        quantity = cleaned_data.get('quantity')

        if product and quantity:
            cleaned_data['subtotal'] = product.price * quantity

        return cleaned_data

OrderItemFormSet = forms.inlineformset_factory(Order, OrderItem, form = OrderItemForm, extra=1)
    