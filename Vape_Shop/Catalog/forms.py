from django import forms

from .models import Offer


class OfferForm(forms.ModelForm):

    class Meta:
        model = Offer
        fields = '__all__'
        widgets = {
            'model': forms.TextInput(attrs={'class': 'br-rad'}),
            'price': forms.NumberInput(attrs={'class': 'br-rad'}),
            'description': forms.Textarea(attrs={'class': 'br-rad'}),
            'photo': forms.FileInput(attrs={'class': 'br-rad'}),
        }
