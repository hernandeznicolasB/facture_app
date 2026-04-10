# GestoPro — Gestion de produits et factures

Application Django permettant de gérer des produits et de générer des factures.

## Fonctionnalités

### Produits
- Créer, modifier, supprimer et afficher des produits
- Chaque produit contient : id, nom, prix, date de péremption
- Indication visuelle si le produit est périmé
- Recherche par nom
- Pagination (10 produits par page)

### Factures
- Créer une facture avec un ou plusieurs produits
- Définir la quantité pour chaque produit
- Récapitulatif dynamique en temps réel lors de la création
- Page de détail : liste des produits, total articles, total à payer
- Pagination (10 factures par page)

## Installation

```bash
# Cloner le repo
git clone <url-du-repo>
cd facture_app

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Installer Django
pip install django

# Appliquer les migrations
python manage.py migrate

# (Optionnel) Données de démonstration
python manage.py loaddata fixtures/demo.json

# Lancer le serveur
python manage.py runserver
```

Accéder à l'application : http://127.0.0.1:8000

## Stack technique
- **Backend** : Django / Python
- **Base de données** : SQLite
- **Frontend** : HTML / CSS / JavaScript vanilla

## Structure du projet
```
facture_app/
├── facture_app/        # Configuration Django
├── produits/           # App gestion des produits
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── factures/           # App gestion des factures
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── templates/          # Templates HTML
│   ├── base.html
│   ├── produits/
│   └── factures/
└── static/css/         # Styles CSS
```
