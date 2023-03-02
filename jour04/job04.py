class Forme:
    def aire(self):
        return 0
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        
    def aire(self):
        print(self.largeur * self.hauteur)
rectangle = Rectangle(5, 10)
print(rectangle.aire())
