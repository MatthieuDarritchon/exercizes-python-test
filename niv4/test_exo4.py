import unittest

from niv4.exo4 import lignes


class MyTestCase(unittest.TestCase):
    def test_ligne_3_0(self):
        resultat_attendu = "33333"
        resultat = lignes(3, 0)
        self.assertEqual(resultat_attendu, resultat, "pb lors de la création de la ligne")

    def test_ligne_3_1(self):
        resultat_attendu = "32223"
        resultat = lignes(3, 1)
        self.assertEqual(resultat_attendu, resultat, "pb lors de la création de la ligne")

    def test_ligne_3_2(self):
        resultat_attendu = "32123"
        resultat = lignes(3, 2)
        self.assertEqual(resultat_attendu, resultat, "pb lors de la création de la ligne")

    def test_ligne_unique_3_0(self):
        resultat_attendu = "33333"
        resultat = lignes(3, 0)
        self.assertEqual(resultat_attendu, resultat, "pb lors de la création de la ligne")

    def test_ligne_unique_3_1(self):
        resultat_attendu = "32223"
        resultat = lignes(3, 1)
        self.assertEqual(resultat_attendu, resultat, "pb lors de la création de la ligne")

    def test_ligne_unique_3_2(self):
        resultat_attendu = "32123"
        resultat = lignes(3, 2)
        self.assertEqual(resultat_attendu, resultat, "pb lors de la création de la ligne")


if __name__ == '__main__':
    unittest.main()
