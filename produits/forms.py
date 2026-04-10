from django import forms
from .models import Produit

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'prix', 'date_peremption']
        widgets = {
            'date_peremption': forms.DateInput(attrs={'type': 'date'}),
            'nom': forms.TextInput(attrs={'placeholder': 'Nom du produit'}),
            'prix': forms.NumberInput(attrs={'placeholder': '0.00', 'step': '0.01', 'min': '0'}),
        }
