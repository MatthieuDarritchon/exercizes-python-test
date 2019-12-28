# création liste unique à partir de liste début

# création liste occurence à partir de liste début

# creation liste final avec les plus grd element de liste occurence :
# on cherche les indice des plus hauts termes de liste occurence et on append dans
# liste final, liste unique de ces indices

# sort liste finale et print chaque element


def liste_unique(liste_initiale):
    resultat = []
    for i in range(len(liste_initiale)):
        if not liste_initiale[i] in resultat:
            resultat.append(liste_initiale[i])
    return resultat


def compte(L, n):
    nb_occurence = 0
    for s in range(len(L)):
        if L[s] == n:
            nb_occurence += 1
    return nb_occurence


def liste_occurence(liste_initiale):
    resultat = []
    for i in range(len(liste_unique(liste_initiale))):
        resultat.append(compte(liste_initiale, liste_unique(liste_initiale)[i]))
    return resultat


def liste_max(liste):
    maxi = max(liste_occurence(liste))
    resultat = []
    for i in range(len(liste_occurence(liste))):
        if liste_occurence(liste)[i] >= maxi:
            resultat.append(liste_unique(liste)[i])
    resultat.sort()
    return resultat



