def puissance(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        y = puissance(x, n/2)
        return y*y
    else:
        return x * puissance(x, n-1)

x = int(input("Entrez un nombre : "))
n = int(input("Entrez un exposant : "))
print(x, "à la puissance", n, "est égal à", puissance(x, n))
