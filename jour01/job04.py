class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return print("Je suis", self.nom, self.prenom)
personne1 = Personne("Doe", "John")
print(personne1.SePresenter()) 

personne2 = Personne("Dupont", "Jean")
print(personne2.SePresenter()) 
