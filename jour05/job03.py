def longueur(chaine):
    if chaine == "":
        return 0
    else:
        return 1 + longueur(chaine[1:])

chaine = "bonjour"
print("La longueur de la chaîne", chaine, "est", longueur(chaine))
