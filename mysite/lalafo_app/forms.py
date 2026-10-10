from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_name', 'category', 'price', 'phone_number', 'city',
            'type', 'product_image', 'descriptions', 'number_product',
        ]
        labels = {
            'product_name': 'Название',
            'category': 'Категория',
            'price': 'Цена, сом',
            'phone_number': 'Номер телефона',
            'city': 'Город',
            'type': 'Оригинал',
            'product_image': 'Фото',
            'descriptions': 'Описание',
            'number_product': 'Номер продукта',
        }
        widgets = {
            'product_name': forms.TextInput(attrs={'placeholder': 'Например: iPhone 15 Pro'}),
            'price': forms.NumberInput(attrs={'placeholder': '0', 'min': 0}),
            'phone_number': forms.TextInput(attrs={'placeholder': '+996700123456'}),
            'city': forms.TextInput(attrs={'placeholder': 'Бишкек'}),
            'descriptions': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Расскажите о товаре'}),
            'number_product': forms.NumberInput(attrs={'placeholder': '1', 'min': 0}),
            'product_image': forms.FileInput(attrs={'accept': 'image/*'}),
        }