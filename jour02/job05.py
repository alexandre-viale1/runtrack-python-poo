class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    def get_marque(self):
        return self.__marque

    def set_marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque

    def get_modele(self):
        return self.__modele

    def set_modele(self, nouveau_modele):
        self.__modele = nouveau_modele

    def get_annee(self):
        return self.__annee

    def set_annee(self, nouvelle_annee):
        self.__annee = nouvelle_annee

    def get_kilometrage(self):
        return self.__kilometrage

    def set_kilometrage(self, nouveau_kilometrage):
        self.__kilometrage = nouveau_kilometrage

    def demarrer(self):
        if self.verifier_plein() > 5:
            self.__en_marche = True
            print("La voiture a démarré.")
        else:
            print("Impossible de démarrer la voiture. Le réservoir est presque vide.")

    def arreter(self):
        self.__en_marche = False
        print("La voiture s'est arrêtée.")

    def verifier_plein(self):
        return self.__reservoir

ma_voiture = Voiture("Renault", "Clio", 2010, 100000)
ma_voiture.reservoir = 100
ma_voiture.demarrer() 
ma_voiture.arreter() 
