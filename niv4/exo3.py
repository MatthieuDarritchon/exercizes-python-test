alb = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN"
chf = "1234567890"
if __name__ == '__main__':
    nb_lettre = 0
    nb_chiffre = 0
    chaine = str(input("chaine:"))
    for i in range(len(chaine)):
        if chaine[i] in alb:
            nb_lettre += 1
        elif chaine[i] in chf:
            nb_chiffre += 1
    print("Chiffres : {}\nLettres : {}".format(nb_chiffre, nb_lettre))
