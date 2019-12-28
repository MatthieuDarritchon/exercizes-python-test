def compte_vache(champs):
    nb_vache = 0
    for i in range(len(champs)):
        if champs[i] == "#":
            nb_vache += 1
    return nb_vache



if __name__ == '__main__':
    def compte_vache(champs):
        nb_vache = 0
        for i in range(len(champs)):
            if champs[i] == "#":
                nb_vache += 1
        return nb_vache


    n = int(input("n"))
    champ = ""
    for j in range(n):
        u = str(input("u"))
        champ += u
    print(compte_vache(champ))

