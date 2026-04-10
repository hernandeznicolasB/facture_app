from django.db import models
from produits.models import Produit

class Facture(models.Model):
    numero = models.CharField(max_length=50, unique=True, verbose_name="Numéro")
    client = models.CharField(max_length=200, verbose_name="Client")
    date_creation = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, verbose_name="Notes")

    class Meta:
        verbose_name = "Facture"
        verbose_name_plural = "Factures"
        ordering = ['-date_creation']

    def __str__(self):
        return f"Facture {self.numero} - {self.client}"

    def total(self):
        return sum(item.sous_total() for item in self.lignes.all())

    def nombre_total_produits(self):
        return sum(item.quantite for item in self.lignes.all())

    def save(self, *args, **kwargs):
        if not self.numero:
            from django.utils import timezone
            count = Facture.objects.count() + 1
            self.numero = f"FAC-{timezone.now().year}-{count:04d}"
        super().save(*args, **kwargs)


class LigneFacture(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, related_name='lignes')
    produit = models.ForeignKey(Produit, on_delete=models.PROTECT)
    quantite = models.PositiveIntegerField(default=1, verbose_name="Quantité")
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix unitaire")

    class Meta:
        verbose_name = "Ligne de facture"
        verbose_name_plural = "Lignes de facture"

    def __str__(self):
        return f"{self.produit.nom} x{self.quantite}"

    def sous_total(self):
        return self.quantite * self.prix_unitaire

    def save(self, *args, **kwargs):
        if not self.prix_unitaire:
            self.prix_unitaire = self.produit.prix
        super().save(*args, **kwargs)
