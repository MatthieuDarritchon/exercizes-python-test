import unittest

# def liste_unique(liste_initiale):
#     return []
from niv3.exo7 import liste_unique, liste_occurence, compte, liste_max


class MyTestCase(unittest.TestCase):
    liste_initiale = [4, 1, 1, 2, 3]
    liste_vide = []
    liste_initiale_2 = [1,2,1,3,2]

    def test_liste_unique(self):
        resultat_attendu = [4, 1, 2, 3]
        resultat = liste_unique(self.liste_initiale)
        self.assertEqual(resultat_attendu, resultat, "liste unique != resultat obtenu")

    def test_liste_occurence(self):
        resultat_attendu = [1, 2, 1, 1]
        resultat = liste_occurence(self.liste_initiale)
        self.assertEqual(resultat_attendu, resultat, "resultat != liste occurence")

    def test_compte(self):
        resultat_attendu = 2
        resultat = compte(self.liste_initiale, 1)
        self.assertEqual(resultat_attendu, resultat, "pb lors du compte de 1")
        resultat_attendu = 0
        resultat = compte(self.liste_vide, 1)
        self.assertEqual(resultat_attendu, resultat, "pb lors du compte de 1")

    def test_liste_max(self):
        resultat_attendu = [1]
        resultat = liste_max(self.liste_initiale)
        self.assertEqual(resultat_attendu, resultat, "pb lors de la selection des occurences max")
        resultat_attendu = [1, 2]
        resultat = liste_max(self.liste_initiale_2)
        self.assertEqual(resultat_attendu, resultat, "pb lors de la selecion des occurences max")


if __name__ == '__main__':
    unittest.main()
