# Supposons un tableau qui contient uniquement des lettres majuscules de l'alphabet
# La première procédure parcourt le tableau une fois pour chaque lettre de l'alphabet
# La deuxième procédure effectue le calcul de fréquence en un seul parcours du tableau
# La fonction auxiliaire position(lettre) renvoie la position de la lettre
def position(lettre):
    return ord(lettre) - ord('A') + 1

def frequences_26(tableau):
    frequences = [0] * 26
    for lettre in tableau:
        indice = position(lettre) - 1
        frequences[indice] += 1
    return frequences

# Exemple d'utilisation :
tableau = ['A', 'B', 'C', 'A', 'B', 'D']
resultat = frequences_26(tableau)
print("VOICI LE RENDU DE LA FONCTION DES 26 PARCOURS")
print(resultat)

# La console affichera donc que le nombre A est apparu 2 fois, le B 2 fois , etc....
# Comment faire pour afficher une phras pour chaque composante du tableau ?

def frequences_1(tableau):
    frequences = [0] * 26
    for lettre in tableau:
        indice = ord(lettre) - ord('A')
        frequences[indice] += 1
    return frequences

# Exemple d'utilisation :
tableau = ['Z', 'R', 'Q', 'A', 'Z', 'V', 'R', 'Z', 'Q', 'R', 'C', 'I']
resultat = frequences_1(tableau)
print("VOICI LE RENDU DE LA FONCTION DU PARCOURS UNIQUE")
print(resultat)