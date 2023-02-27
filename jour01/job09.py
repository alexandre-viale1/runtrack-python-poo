class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
        
    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)
        
    def afficher(self):
        print("Nom du produit : ", self.nom)
        print("Prix HT : ", self.prixHT)
        print("TVA : ", self.TVA)
        print("Prix TTC : ", self.CalculerPrixTTC())
        
    def modifier_nom(self, nouveau_nom):
        self.nom = nouveau_nom
        
    def modifier_prixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT
        
    def get_nom(self):
        return self.nom
    
    def get_prixHT(self):
        return self.prixHT
    
    def get_TVA(self):
        return self.TVA
    
produit1 = Produit("Ordinateur portable", 800, 20)
produit2 = Produit("Iphone", 900, 10)

produit1.afficher()
produit2.afficher()

produit1.modifier_nom("nouvel ordinateur portable")
produit2.modifier_prixHT(700)

print("Nouveau prix du", produit1.get_nom(), ":", produit1.CalculerPrixTTC())
print("Nouveau prix du", produit2.get_nom(), ":", produit2.CalculerPrixTTC())
