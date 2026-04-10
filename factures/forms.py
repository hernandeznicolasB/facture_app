from django import forms
from django.forms import inlineformset_factory
from .models import Facture, LigneFacture
from produits.models import Produit

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['client', 'notes']
        widgets = {
            'client': forms.TextInput(attrs={'placeholder': 'Nom du client'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Notes optionnelles...'}),
        }

class LigneFactureForm(forms.ModelForm):
    class Meta:
        model = LigneFacture
        fields = ['produit', 'quantite']
        widgets = {
            'quantite': forms.NumberInput(attrs={'min': '1', 'value': '1'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['produit'].queryset = Produit.objects.all()
        self.fields['produit'].empty_label = "-- Sélectionner un produit --"

# extra=0 : Django ne rend AUCUNE ligne vide par défaut, le JS gère tout
LigneFactureFormSet = inlineformset_factory(
    Facture,
    LigneFacture,
    form=LigneFactureForm,
    extra=0,
    can_delete=True,
    min_num=1,
    validate_min=True,
)
