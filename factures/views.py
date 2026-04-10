from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db import transaction
from .models import Facture, LigneFacture
from .forms import FactureForm, LigneFactureFormSet
from produits.models import Produit

def facture_list(request):
    factures = Facture.objects.prefetch_related('lignes').all()
    paginator = Paginator(factures, 10)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'factures/list.html', {'page_obj': page_obj})

def facture_create(request):
    produits = Produit.objects.all()
    if request.method == 'POST':
        form = FactureForm(request.POST)
        formset = LigneFactureFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                facture = form.save()
                formset.instance = facture
                lignes = formset.save(commit=False)
                for ligne in lignes:
                    ligne.prix_unitaire = ligne.produit.prix
                    ligne.save()
                for obj in formset.deleted_objects:
                    obj.delete()
            messages.success(request, f'Facture {facture.numero} créée avec succès.')
            return redirect('facture_detail', pk=facture.pk)
    else:
        form = FactureForm()
        formset = LigneFactureFormSet()
    return render(request, 'factures/form.html', {
        'form': form,
        'formset': formset,
        'produits': produits,
    })

def facture_detail(request, pk):
    facture = get_object_or_404(Facture.objects.prefetch_related('lignes__produit'), pk=pk)
    return render(request, 'factures/detail.html', {'facture': facture})

def facture_delete(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    if request.method == 'POST':
        numero = facture.numero
        facture.delete()
        messages.success(request, f'Facture {numero} supprimée.')
        return redirect('facture_list')
    return render(request, 'factures/confirm_delete.html', {'facture': facture})
