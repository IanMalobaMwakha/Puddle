from django import forms

from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('cartegory', 'name', 'description', 'price', 'image',)
        widgets = {
            'cartegory': forms.Select(attrs={
                'class': INPUT_CLASSES
            })
        }