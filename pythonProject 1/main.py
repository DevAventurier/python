
print("Entrez 3 entiers:")
valeurs = []
for i in range(3): # la boucle ci oblige lutilisateur a entrer un nombre dentiers predefinis
    num = int(input()) # demande à l'utilisateur de saisir un entier
    valeurs.append(num) # ajoute l'entier à la liste des nombres

# Initialisons les compteurs pour les nombres pairs et impairs a zero
pair = 0
impair = 0

for num in valeurs: # la boucle parcours la liste des  nombres saisis par lutilisateur et determine leur parite
    if num % 2 == 0: # condition pour verifier si le nombre saisi est pair ou pas
        pair += 1 # incrémente le contenu de la variable stockant les nombres pairs
    else:
        impair += 1 # si cette section de la boucle est appele cela veu dire que le nombre nest pas pair et donc il est forcement impair

# Le resultat apres tri est ensuite afficher a lutilisateur
print("Les donnees saisies sont de ", pair, "pairs et",impair, "impairs")

