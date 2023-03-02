class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0
        
    def marquerUnBut(self):
        self.buts_marques += 1
        
    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1
        
    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1
        
    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1
        
    def afficherStatistiques(self):
        print("Statistiques de ", self.nom)
        print("Nombre de buts marqués :", self.buts_marques)
        print("Nombre de passes décisives :", self.passes_decisives)
        print("Nombre de cartons jaunes reçus :", self.cartons_jaunes)
        print("Nombre de cartons rouges reçus :", self.cartons_rouges)


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.liste_joueurs = []
        
    def ajouterJoueur(self, joueur):
        self.liste_joueurs.append(joueur)
        
    def afficherStatistiquesJoueurs(self):
        print("Statistiques de l'équipe", self.nom)
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()
            
    def mettreAJourStatistiquesJoueur(self, nom_joueur, action):
        for joueur in self.liste_joueurs:
            if joueur.nom == nom_joueur:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "rouge":
                    joueur.recevoirUnCartonRouge()
                else:
                    print("Action invalide")
                break

j1_e1 = Joueur("Ronaldo", 7, "Attaquant")
j2_e1 = Joueur("Messi", 10, "Attaquant")
j3_e1 = Joueur("Neymar", 11, "Attaquant")
j4_e1 = Joueur("Mbappé", 9, "Attaquant")
j5_e1 = Joueur("Payet", 6, "Milieu")
j6_e1 = Joueur("Pogba", 8, "Milieu")
j7_e1 = Joueur("Varane", 4, "Défenseur")
j8_e1 = Joueur("Lenglet", 5, "Défenseur")
j9_e1= Joueur("Kimpembe", 3, "Défenseur")
j10_e1 = Joueur("Lloris", 1, "Gardien")
j1_e2 = Joueur("Ángel" , 5, "Attaquant")
j2_e2 = Joueur("Michael", 8, "Attaquant")
j3_e2 = Joueur("Romario", 4, "Attaquant")
j4_e2 = Joueur("Ayrton", 3, "Attaquant")
j5_e2 = Joueur("Carlos", 11, "Milieu")
j6_e2 = Joueur("José",12 ,"Milieu")
j7_e2 = Joueur("Robert",7 ,"Défenseur")
j8_e2 = Joueur("Piero", 1 , "Défenseur")
j9_e2 = Joueur("Félix", 10 , "Défenseur")
j10_e2 = Joueur("Hernán", 1, "Gardient")

equipe1 = Equipe("Equipe 1")
equipe2 = Equipe("Equipe 2")

equipe1.ajouterJoueur(j1_e1)
equipe1.ajouterJoueur(j2_e1)
equipe1.ajouterJoueur(j3_e1)
equipe1.ajouterJoueur(j4_e1)
equipe1.ajouterJoueur(j5_e1)
equipe1.ajouterJoueur(j6_e1)
equipe1.ajouterJoueur(j7_e1)
equipe1.ajouterJoueur(j8_e1)
equipe1.ajouterJoueur(j9_e1)
equipe1.ajouterJoueur(j10_e1)

equipe2.ajouterJoueur(j1_e2)
equipe2.ajouterJoueur(j2_e2)
equipe2.ajouterJoueur(j3_e2)
equipe2.ajouterJoueur(j4_e2)
equipe2.ajouterJoueur(j5_e2)
equipe2.ajouterJoueur(j6_e2)
equipe2.ajouterJoueur(j7_e2)
equipe2.ajouterJoueur(j8_e2)
equipe2.ajouterJoueur(j9_e2)
equipe2.ajouterJoueur(j10_e2)

equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

equipe1.mettreAJourStatistiquesJoueur("Ronaldo", "but")
equipe1.mettreAJourStatistiquesJoueur("Messi", "passe")
equipe1.mettreAJourStatistiquesJoueur("Kante", "jaune")
equipe2.mettreAJourStatistiquesJoueur("Micheal", "jaune")
equipe2.mettreAJourStatistiquesJoueur("Romario", "rouge")

equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()