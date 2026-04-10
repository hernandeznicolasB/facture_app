from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=200, verbose_name="Nom")
    prix = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix (€)")
    date_peremption = models.DateField(verbose_name="Date de péremption")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"
        ordering = ['nom']

    def __str__(self):
        return f"{self.nom} - {self.prix}€"

    def est_perime(self):
        from django.utils import timezone
        return self.date_peremption < timezone.now().date()
