class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

    def getLongueur(self):
        return self.__longueur

    def setLongueur(self, longueur):
        self.__longueur = longueur

    def getLargeur(self):
        return self.__largeur

    def setLargeur(self, largeur):
        self.__largeur = largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__longueur = longueur
        self.__largeur = largeur
        self.__hauteur = hauteur

    def volume(self):
        return self.surface() * self.__hauteur

    def getHauteur(self):
        return self.__hauteur

    def setHauteur(self, hauteur):
        self.__hauteur = hauteur
r = Rectangle(longueur=5, largeur=3)

print("Longueur :", r.getLongueur())
print("Largeur :", r.getLargeur())
print("Périmètre :", r.perimetre())
print("Surface :", r.surface())

r.setLongueur(7)
r.setLargeur(4)

print("Nouvelle longueur :", r.getLongueur())
print("Nouvelle largeur :", r.getLargeur())
print("Nouveau périmètre :", r.perimetre())
print("Nouvelle surface :", r.surface())

p = Parallelepipede(longueur=5, largeur=3, hauteur=2)

print("Longueur :", p.getLongueur())
print("Largeur :", p.getLargeur())
print("Hauteur :", p.getHauteur())
print("Périmètre :", p.perimetre())
print("Surface :", p.surface())
print("Volume :", p.volume())

p.setLongueur(7)
p.setLargeur(4)
p.setHauteur(3)

print("Nouvelle longueur :", p.getLongueur())
print("Nouvelle largeur :", p.getLargeur())
print("Nouvelle hauteur :", p.getHauteur())
print("Nouveau périmètre :", p.perimetre())
print("Nouvelle surface :", p.surface())
print("Nouveau volume :", p.volume())
