import unittest
from random import randint

import main as eleve

msg = "erreur de test avec les valeurs de l'exemple"


class Exo_pythagore(unittest.TestCase):    
    def test_exemples1(self):
        info = msg + '\nle triangle (3,4,5) est rectangle'
        self.assertTrue(eleve.test_pythagore(3,4,5), msg= info)

    def test_exemples2(self):
        info = msg + '\nle triangle (3,5,4) est rectangle'
        self.assertTrue(eleve.test_pythagore(3,5,4), msg= info)

    def test_exemples3(self):
        info = msg + '\nle triangle (5,4,3) est rectangle'
        self.assertTrue(eleve.test_pythagore(5, 4, 3), msg= info) 

    def test_exemples4(self):
        info = msg + '\nle triangle (7,2,12) est rectangle'
        self.assertFalse(eleve.test_pythagore(7,2,12), msg= info)

    def tri_rect_aleatoire():
        a = randint(1, 200)
        while True:
            for b in range(a):
                for c in range(a):
                    if b*b + c*c == a*a:
                        return (b, c, a)
            a += 1

    def test_est_rect(self):
        for i in range(5):
            a, b, c = Exo_pythagore.tri_rect_aleatoire()
            
            info = msg + "\nle triangle ("+str(a)+","+str(b)+","+str(c)+") est rectangle"
            self.assertTrue(eleve.test_pythagore(a, b, c), msg= info)

    def test_non_rect(self):
        for i in range(5):
            a, b, c = Exo_pythagore.tri_rect_aleatoire()
            c += 1
            info = msg + "\nle triangle ("+str(a)+","+str(b)+","+str(c)+") n'est pas rectangle"
            self.assertFalse(eleve.test_pythagore(a, b, c), msg= info)


class Exo_valeur_absolue(unittest.TestCase):
    def test_exemple_1(self):
        info = msg + '\nla valeur absolue de 5 est 5'
        self.assertEqual(eleve.valeur_absolue(5), 5, msg=info)

    def test_exemple_2(self):
        info = msg + '\nla valeur absolue de -5 est 5'
        self.assertEqual(eleve.valeur_absolue(-5), 5, msg=info)

    def test_exemple_3(self):
        info = msg + '\nla valeur absolue de 0 est 0'
        self.assertEqual(eleve.valeur_absolue(0), 0, msg=info)

    def test_exemple_4(self):
        info = msg + '\nla valeur absolue de -42 est 42'
        self.assertEqual(eleve.valeur_absolue(-42), 42, msg=info)

    def test_alea(self):
        n = 100
        for _ in range(n):
            x = randint(-10**10, 10**10)
            rep = x if x >=0 else -x
            info = msg + '\nla valeur absolue de '+str(x)+' est '+str(rep)
            self.assertEqual(eleve.valeur_absolue(x), rep, msg=info)


class Exo_multiples(unittest.TestCase):

    def test_exemples1(self):
        info = msg + "\nla somme des multiples jusqu'à 2 inclus vaut 0"
        self.assertEqual(eleve.multiples_3_ou_5(2), 0, msg= info)

    def test_exemples2(self):
        info = msg + "\nla somme des multiples jusqu'à 6 inclus vaut 14"
        self.assertEqual(eleve.multiples_3_ou_5(6), 14, msg= info)

    def test_exemples3(self):
        info = msg + "\nla somme des multiples jusqu'à 10 inclus vaut 33"
        self.assertEqual(eleve.multiples_3_ou_5(10), 33, msg= info)

    def test_exemples4(self):
        info = msg + "\nla somme des multiples jusqu'à 100 inclus vaut 2418"
        self.assertEqual(eleve.multiples_3_ou_5(100), 2418, msg= info)

    def rep(borne_sup):
        somme = 0
        for i in range(borne_sup+1):
            if i % 3 == 0 or i % 5 == 0:
                somme += i
        return somme

    def test_alea(self):
        for _ in range(100):
            x = randint(0, 1000)
            rep = Exo_multiples.rep(x)
            info = msg + "\nla somme des multiples jusqu'à "+str(x)+" inclus vaut "+str(rep)
            self.assertEqual(eleve.multiples_3_ou_5(x), rep, msg= info)



if __name__ == '__main__':
    unittest.main()
