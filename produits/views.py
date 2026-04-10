from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Produit
from .forms import ProduitForm

def produit_list(request):
    produits = Produit.objects.all()
    search = request.GET.get('search', '')
    if search:
        produits = produits.filter(nom__icontains=search)
    
    paginator = Paginator(produits, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'produits/list.html', {
        'page_obj': page_obj,
        'search': search,
    })

def produit_create(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            produit = form.save()
            messages.success(request, f'Produit "{produit.nom}" créé avec succès.')
            return redirect('produit_list')
    else:
        form = ProduitForm()
    return render(request, 'produits/form.html', {'form': form, 'action': 'Créer'})

def produit_edit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            messages.success(request, f'Produit "{produit.nom}" modifié avec succès.')
            return redirect('produit_list')
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'produits/form.html', {'form': form, 'action': 'Modifier', 'produit': produit})

def produit_delete(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    # Vérifier si le produit est utilisé dans des factures
    factures_liees = produit.lignesfacture_set.select_related('facture').all() if hasattr(produit, 'lignesfacture_set') else []
    # Récupérer via la relation inverse correcte
    from factures.models import LigneFacture
    lignes = LigneFacture.objects.filter(produit=produit).select_related('facture')
    
    if request.method == 'POST':
        if lignes.exists():
            messages.error(request, f'Impossible de supprimer "{produit.nom}" : ce produit est utilisé dans {lignes.count()} facture(s).')
            return redirect('produit_list')
        nom = produit.nom
        produit.delete()
        messages.success(request, f'Produit "{nom}" supprimé avec succès.')
        return redirect('produit_list')
    return render(request, 'produits/confirm_delete.html', {'produit': produit, 'lignes': lignes})
