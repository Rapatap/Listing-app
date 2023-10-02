from django import forms
from .models import ListingItem

class ListingForm(forms.ModelForm):
    class Meta:
        model = ListingItem
        fields = ['title', 'description', 'price', 'image', 'video']
