
from app import mongo

class Produit:
    def __init__(self, nom, description, prix):
        self.nom = nom
        self.description = description
        self.prix = prix

class Commentaire:
    def __init__(self, produit_id, texte, positif):
        self.produit_id = produit_id
        self.texte = texte
        self.positif = positif