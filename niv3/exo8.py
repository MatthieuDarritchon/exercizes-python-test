def moyenne(liste_initiale):
    somme = 0
    liste_finale = []
    for i in range(len(liste_initiale)):
        somme += liste_initiale[i]
    moy = somme / len(liste_initiale)
    for j in range(len(liste_initiale)):
        if liste_initiale[j] <= moy:
            liste_finale.append(liste_initiale[j])
    return liste_finale
