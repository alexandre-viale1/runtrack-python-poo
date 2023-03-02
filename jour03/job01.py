class Ville:
    def __init__(self, nom, population):
        self.nom = nom
        self.population = population
        
    def ajouter_population(self):
        self.population += 1
        
class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville
        
    def ajouter_population(self):
        self.ville.ajouter_population()

ville_paris = Ville("Paris", 1000000)
print("Population de la ville de Paris:", ville_paris.population, "habitants")

ville_marseille = Ville("Marseille", 861635)
print("Population de la ville de Marseille:", ville_marseille.population, "habitants")

john = Personne("John", 45, ville_paris)
john.ajouter_population()

myrtille = Personne("Myrtille", 4, ville_paris)
myrtille.ajouter_population()

chloe = Personne("Chloé", 18, ville_marseille)
chloe.ajouter_population()

print("Mise a jour de la population de la ville de Paris", ville_paris.population, "habitants")
print("Mise a jour de la population de la ville de Marseille", ville_marseille.population, "habitants")