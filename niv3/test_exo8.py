import unittest

from niv3.exo8 import moyenne


class MyTestCase(unittest.TestCase):
    liste_initiale = [1, 2, 3, 1]
    liste_initiale2 = [1, 2, 3]

    def test_moyenne(self):
        resultat_attendu = [1, 1]
        resultat = moyenne(self.liste_initiale)
        self.assertEqual(resultat_attendu, resultat, "pb lors du calcul de la moy")

    def test_moyenne_entiere(self):
        resultat_attendu = [1, 2]
        resultat = moyenne(self.liste_initiale2)
        self.assertEqual(resultat_attendu, resultat, "pb lors du calcul de la moy")


if __name__ == '__main__':
    unittest.main()
