import unittest

from niv4.exo2 import compte_vache


class MyTestCase(unittest.TestCase):
    champs = '#""#|;;#""""'

    def test_something(self):
        resultat_attendu = 3
        resultat = compte_vache(self.champs)
        self.assertEqual(resultat_attendu, resultat, 'pb lors du compte des vaches')


if __name__ == '__main__':
    unittest.main()
