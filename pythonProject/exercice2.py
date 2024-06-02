# la fonction test prend un nombre entier n en entrée
# Ce nombre est converti en chaîne de caractères à l'aide de la fonction str()
# Ensuite, la chaîne de caractères est inversée comme précédemment
# Enfin, la fonction vérifie si la chaîne originale et son inversion sont égales
#  Si elles le sont, la fonction retourne True, sinon elle retourne False

def test(n):
    # Convertir le nombre en chaîne de caractères pour pouvoir inverser ses chiffres
    num_str = str(n)

    # Inverser la chaîne de caractères représentant le nombre
    reverse = num_str[::-1]

    # Vérifier si le nombre est égal à son inversion
    if num_str == reverse:
        return True
    return False


# Exemples d'utilisation
print(test(1001))
print(test(11))
print(test(44))
print(test(101))
print(test(141))
print(test(102))
print(test(6368347))
# On constatera que seul les 5 premiers sont des paliundromes

