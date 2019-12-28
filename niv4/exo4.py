def lignes(n, ligne):
    liste = []
    chaine = ""
    if ligne == 0:
        for i in range(2 * n - 1):
            liste.append(n)
        for k in range(len(liste)):
            chaine += "{}".format(liste[k])
        return chaine
    elif ligne == 1:
        for j in range(2 * n - 1):
            liste.append(n - 1)
        liste[0] = n
        liste[len(liste) - 1] = n
        for k in range(len(liste)):
            chaine += "{}".format(liste[k])
        return chaine
    elif ligne == 2:
        for m in range(2 * n - 1):
            liste.append(n - 2)
        liste[0] = n
        liste[1] = n - 1
        liste[len(liste) - 1 - 1] = n - 1
        liste[len(liste) - 1] = n
        for k in range(len(liste)):
            chaine += "{}".format(liste[k])
        return chaine


def ligne_unique(n, ligne):
    liste = []
    chaine = ""
    if ligne == 0:
        for i in range(2 * n - 1):
            liste.append(n)
        for k in range(len(liste)):
            chaine += "{}".format(liste[k])
        return chaine
    else:
        for j in range(2 * n - 1):
            liste.append(n - ligne)
        for a in range(ligne):
            liste[a] = n - a
            liste[len(liste) - 1 - a] = n - a
        for b in range(len(liste)):
            chaine += "{}".format(liste[b])
        return chaine
