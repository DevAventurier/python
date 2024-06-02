def tri_bulle(tableau):
    n = len(tableau)

    for i in range(n - 1):
        min = i

        # Recherchons l'indice du plus petit élément
        for j in range(i + 1, n):
            if tableau[j] < tableau[min]:
                min = j

        # Intervertissons les emplacements
        tableau[i], tableau[min] = tableau[min], tableau[i]

    return tableau


# Exemple d'utilisation
tableau = [0, 13, 7, 56, 21, 9]
tableau_trie = tri_bulle(tableau)
print(tableau_trie)

# L'exemple ci trie le tableau  en utilisant la fonction et le tableau trié est affiché avec des elements dans un ordre croissant.