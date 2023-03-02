class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f"L'élève a {self.age} ans")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print(f"L'élève a {self.age} ans")


class Professeur(Personne):
    def __init__(self, matiereEnseignee, age=30):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")

personne = Personne()
jean = Eleve()


jean.afficherAge()

