class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True

    def get_titre(self):
        return self.__titre

    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nb_pages(self):
        return self.__nb_pages

    def set_nb_pages(self, nb_pages):
        if nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            print("Le nombre de pages doit être un entier positif.")

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est pas disponible.")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre n'a pas été emprunté.")

    def __str__(self):
        return "{} de {} contient {} pages".format(self.__titre, self.__auteur, self.__nb_pages)

livre1 = Livre("Harry Potter à l'école des sorciers", "J. K. Rowling", 305)
print(livre1)

print(livre1.verification())#on verifie que le livre est disponible True/False


livre1.emprunter()#on emprunte le livre


print(livre1.verification())#on reverifie si le livre est disponible


livre1.emprunter()# on ressaye si on peut emprunter le livre


livre1.rendre()#on rend le livre afin qu'il soit a nouveau disponible


print(livre1.verification())#on verifie une derniere fois que le livre est disponible