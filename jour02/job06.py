class Commande:
    def __init__(self, num_commande):
        self.__num_commande = num_commande
        self.__plats = {}
        self.__statut = "en cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        self.__plats[nom_plat] = {"prix": prix_plat, "statut": "en cours"}

    def annuler_commande(self):
        self.__statut = "annulée"

    def __calculer_total(self):
        total = 0
        for plat in self.__plats:
            if self.__plats[plat]["statut"] == "en cours":
                total += self.__plats[plat]["prix"]
        return total

    def afficher_commande(self):
        print(f"Commande n°{self.__num_commande}")
        for plat in self.__plats:
            print(f"- {plat}: {self.__plats[plat]['prix']}€ ({self.__plats[plat]['statut']})")
        total = self.__calculer_total()
        print(f"Total: {total}€")

    def calculer_TVA(self, taux_TVA):
        total = self.__calculer_total()
        TVA = total * taux_TVA / 100
        return TVA


commande1 = Commande(1)

commande1.ajouter_plat("Pizza Margherita", 10)
commande1.ajouter_plat("Spaghetti Carbonara", 12)
commande1.ajouter_plat("Tiramisu", 6)

commande1.afficher_commande()

TVA = commande1.calculer_TVA(20)
print(f"TVA: {TVA}€")




commande2 = Commande(2)

commande2.ajouter_plat("risotto alla milanese", 18)
commande2.ajouter_plat("Spaghetti Carbonara", 12)
commande2.ajouter_plat("Panna cotta", 8)

commande2.afficher_commande()

TVA = commande2.calculer_TVA(20)
print(f"TVA: {TVA}€")