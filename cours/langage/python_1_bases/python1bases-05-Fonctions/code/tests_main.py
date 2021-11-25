import unittest
from random import randint, choice

import main as eleve
import main as prof

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

    @staticmethod
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


class Exo_max2(unittest.TestCase):
    def test_exemple_1(self):
        info = msg + "\nle max de (0,0) vaut 0"
        self.assertEqual(eleve.max2(0,0), 0, msg= info)

    def test_exemple_2(self):
        info = msg + "\nle max de (1, 2) vaut 2"
        self.assertEqual(eleve.max2(1, 2), 2, msg= info)

    def test_exemple_3(self):
        info = msg + "\nle max de (-2, -1) vaut -1"
        self.assertEqual(eleve.max2(-2,-1), -1, msg= info)

    def test_alea(self):
        for _ in range(100):
            a = randint(-10**10, 10**10)
            b = randint(-10**10, 10**10)
            rep = max(a, b)
            info = msg + "\nle max de ("+str(a)+", "+str(b)+") vaut "+str(rep)
            self.assertEqual(eleve.max2(a, b), rep, msg= info)


class Exo_max3(unittest.TestCase):
    def test_exemple_1(self):
        info = msg + "\nle max de (0,0,0) vaut 0"
        self.assertEqual(eleve.max3(0,0,0), 0, msg= info)

    def test_exemple_2(self):
        info = msg + "\nle max de (0,5,2) vaut 5"
        self.assertEqual(eleve.max3(0,5,2),5, msg= info)

    def test_exemple_3(self):
        info = msg + "\nle max de (-10,5,21) vaut 21"
        self.assertEqual(eleve.max3(-10,5,21), 21, msg= info)

    def test_alea(self):
        for _ in range(100):
            a = randint(-10**10, 10**10)
            b = randint(-10**10, 10**10)
            c = randint(-10**10, 10**10)
            rep = max(a, b, c)
            info = msg + "\nle max de ("+str(a)+", "+str(b)+", "+str(c)+") vaut "+str(rep)
            self.assertEqual(eleve.max3(a, b, c), rep, msg= info)


class Exo_puissance(unittest.TestCase):    
    def test_exemple_1(self):
        info = msg + "\n5 puissance 2 vaut 25"
        self.assertEqual(eleve.puissance(5, 2), 5**2, msg= info)
    
    def test_exemple_2(self):
        info = msg + "\n100 puissance 0 vaut 1"
        self.assertEqual(eleve.puissance(100, 0), 1, msg= info)
    
    def test_exemple_3(self):
        info = msg + "\n2 puissance 10 vaut 1024"
        self.assertEqual(eleve.puissance(2, 10), 1024, msg= info)
    
    def test_alea(self):
        for _ in range(100):
            a = randint(0, 10**10)
            b = randint(0, 100)
            rep = a**b
            info = msg + "\n"+str(a)+" puissance "+str(b)+" vaut "+str(rep)
            self.assertEqual(eleve.puissance(a, b), rep, msg=info)


class Exo_est_bissextile(unittest.TestCase):    
    def test_exemple_1(self):
        info = msg + "\nl'année 1996 est bissextile"
        self.assertTrue(eleve.est_bissextile(1996), msg= info)
    def test_exemple_2(self):
        info = msg + "\nl'année 2024 est bissextile"
        self.assertTrue(eleve.est_bissextile(2024), msg= info)
    def test_exemple_3(self):
        info = msg + "\nl'année 2021 n'est pas bissextile"
        self.assertFalse(eleve.est_bissextile(2021), msg= info)
    def test_alea(self):
        annees_bissextiles = [1584, 1588, 1592, 1596, 1600, 1604, 1608, 1612, 1616, 1620, 1624, 1628, 1632, 1636, 1640, 1644, 1648, 1652, 1656, 1660, 1664, 1668, 1672, 1676, 1680, 1684, 1688, 1692, 1696, 1704, 1708, 1712, 1716, 1720, 1724, 1728, 1732, 1736, 1740, 1744, 1748, 1752, 1756, 1760, 1764, 1768, 1772, 1776, 1780, 1784, 1788, 1792, 1796, 1804, 1808, 1812, 1816, 1820, 1824, 1828, 1832, 1836, 1840, 1844, 1848, 1852, 1856, 1860, 1864, 1868, 1872, 1876, 1880, 1884, 1888, 1892, 1896, 1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096, 2104, 2108, 2112, 2116, 2120, 2124, 2128, 2132, 2136, 2140, 2144, 2148, 2152, 2156, 2160, 2164, 2168, 2172, 2176, 2180, 2184, 2188, 2192, 2196, 2204, 2208, 2212, 2216, 2220, 2224, 2228, 2232, 2236, 2240, 2244, 2248, 2252, 2256, 2260, 2264, 2268, 2272, 2276, 2280, 2284, 2288, 2292, 2296, 2304, 2308, 2312, 2316, 2320, 2324, 2328, 2332, 2336, 2340, 2344, 2348, 2352, 2356, 2360, 2364, 2368, 2372, 2376, 2380, 2384, 2388, 2392, 2396, 2400, 2404, 2408, 2412, 2416, 2420, 2424, 2428, 2432, 2436, 2440, 2444, 2448, 2452, 2456, 2460, 2464, 2468, 2472, 2476, 2480, 2484, 2488, 2492, 2496, 2504, 2508, 2512, 2516, 2520, 2524, 2528, 2532, 2536, 2540, 2544, 2548, 2552, 2556, 2560, 2564, 2568, 2572, 2576, 2580, 2584, 2588, 2592, 2596, 2604, 2608, 2612, 2616, 2620, 2624, 2628, 2632, 2636, 2640, 2644, 2648, 2652, 2656, 2660, 2664, 2668, 2672, 2676, 2680, 2684, 2688, 2692, 2696, 2704, 2708, 2712, 2716, 2720, 2724, 2728, 2732, 2736, 2740, 2744, 2748, 2752, 2756, 2760, 2764, 2768, 2772, 2776, 2780, 2784, 2788, 2792, 2796, 2800, 2804, 2808, 2812, 2816, 2820, 2824, 2828, 2832, 2836, 2840, 2844, 2848, 2852, 2856, 2860, 2864, 2868, 2872, 2876, 2880, 2884, 2888, 2892, 2896, 2904, 2908, 2912, 2916, 2920, 2924, 2928, 2932, 2936, 2940, 2944, 2948, 2952, 2956, 2960, 2964, 2968, 2972, 2976, 2980, 2984, 2988, 2992, 2996]
        for _ in range(50):
            annee = choice(annees_bissextiles)
            info = msg + "\nl'année "+str(annee)+" est bissextile"
            self.assertTrue(eleve.est_bissextile(annee), msg= info)
        for _ in range(50):
            annee = randint(1584, 2996)
            rep = annee in annees_bissextiles
            info = msg + "\nréponse incorrecte pour l'année "+str(annee)
            self.assertEqual(eleve.est_bissextile(annee), rep, msg=info)
            

class Exo_nb_jours_annee(unittest.TestCase):    
    def test_exemple_1(self):
        info = msg + "\nl'année 1996 à 366 jours"
        self.assertEqual(eleve.nb_jours_annee(1996), 366, msg= info)
    def test_exemple_2(self):
        info = msg + "\nl'année 2024 est bissextile"
        self.assertEqual(eleve.nb_jours_annee(2024), 366, msg= info)
    def test_exemple_3(self):
        info = msg + "\nl'année 2021 n'est pas bissextile"
        self.assertEqual(eleve.nb_jours_annee(2021), 365, msg= info)
    def test_alea(self):
        annees_bissextiles = [1584, 1588, 1592, 1596, 1600, 1604, 1608, 1612, 1616, 1620, 1624, 1628, 1632, 1636, 1640, 1644, 1648, 1652, 1656, 1660, 1664, 1668, 1672, 1676, 1680, 1684, 1688, 1692, 1696, 1704, 1708, 1712, 1716, 1720, 1724, 1728, 1732, 1736, 1740, 1744, 1748, 1752, 1756, 1760, 1764, 1768, 1772, 1776, 1780, 1784, 1788, 1792, 1796, 1804, 1808, 1812, 1816, 1820, 1824, 1828, 1832, 1836, 1840, 1844, 1848, 1852, 1856, 1860, 1864, 1868, 1872, 1876, 1880, 1884, 1888, 1892, 1896, 1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096, 2104, 2108, 2112, 2116, 2120, 2124, 2128, 2132, 2136, 2140, 2144, 2148, 2152, 2156, 2160, 2164, 2168, 2172, 2176, 2180, 2184, 2188, 2192, 2196, 2204, 2208, 2212, 2216, 2220, 2224, 2228, 2232, 2236, 2240, 2244, 2248, 2252, 2256, 2260, 2264, 2268, 2272, 2276, 2280, 2284, 2288, 2292, 2296, 2304, 2308, 2312, 2316, 2320, 2324, 2328, 2332, 2336, 2340, 2344, 2348, 2352, 2356, 2360, 2364, 2368, 2372, 2376, 2380, 2384, 2388, 2392, 2396, 2400, 2404, 2408, 2412, 2416, 2420, 2424, 2428, 2432, 2436, 2440, 2444, 2448, 2452, 2456, 2460, 2464, 2468, 2472, 2476, 2480, 2484, 2488, 2492, 2496, 2504, 2508, 2512, 2516, 2520, 2524, 2528, 2532, 2536, 2540, 2544, 2548, 2552, 2556, 2560, 2564, 2568, 2572, 2576, 2580, 2584, 2588, 2592, 2596, 2604, 2608, 2612, 2616, 2620, 2624, 2628, 2632, 2636, 2640, 2644, 2648, 2652, 2656, 2660, 2664, 2668, 2672, 2676, 2680, 2684, 2688, 2692, 2696, 2704, 2708, 2712, 2716, 2720, 2724, 2728, 2732, 2736, 2740, 2744, 2748, 2752, 2756, 2760, 2764, 2768, 2772, 2776, 2780, 2784, 2788, 2792, 2796, 2800, 2804, 2808, 2812, 2816, 2820, 2824, 2828, 2832, 2836, 2840, 2844, 2848, 2852, 2856, 2860, 2864, 2868, 2872, 2876, 2880, 2884, 2888, 2892, 2896, 2904, 2908, 2912, 2916, 2920, 2924, 2928, 2932, 2936, 2940, 2944, 2948, 2952, 2956, 2960, 2964, 2968, 2972, 2976, 2980, 2984, 2988, 2992, 2996]
        for _ in range(50):
            annee = choice(annees_bissextiles)
            info = msg + "\nl'année "+str(annee)+" est bissextile"
            self.assertEqual(eleve.nb_jours_annee(annee), 366, msg= info)
        for _ in range(50):
            annee = randint(1584, 2996)
            rep = 366 if annee in annees_bissextiles else 365
            info = msg + "\nréponse incorrecte pour l'année "+str(annee)
            self.assertEqual(eleve.nb_jours_annee(annee), rep, msg=info)
            

class Exo_nb_jours_mois(unittest.TestCase):    
    def test_exemple_1(self):
        info = msg + "\nen janvier 1900, il y a 31 jours"
        self.assertEqual(eleve.nb_jours_mois(1900,1), 31, msg= info)
   
    def test_exemple_2(self):
        info = msg + "\nen février 1900, il y a 28 jours"
        self.assertEqual(eleve.nb_jours_mois(1900,2), 28, msg= info)
   
    def test_exemple_3(self):
        info = msg + "\nen février 1904, il y a 29 jours"
        self.assertEqual(eleve.nb_jours_mois(1904,2), 29, msg= info)  
 
    def test_exemple_4(self):
        info = msg + "\nen septembre 2021, il y a 30 jours"
        self.assertEqual(eleve.nb_jours_mois(2021,9), 30, msg= info)
    
    def test_alea(self):
        for _ in range(100):
            annee = randint(1600, 2300)
            mois  = randint(1, 12)
            rep_eleve = eleve.nb_jours_mois(annee, mois)
            rep_prof  = prof.nb_jours_mois(annee, mois)
            info = msg + "\nle mois "+str(mois)+" de l'année "+str(annee)+" admet "+str(rep_prof)+" jours"
            self.assertEqual(rep_eleve, rep_prof, msg=info)
           
         
class Exo_nb_jours(unittest.TestCase):    
    def test_exemple_1(self):
        info = msg + "\nentre le 1/1/2021 et le 15/1/2021 il y a 15 jours"
        self.assertEqual(eleve.nb_jours(1,1,2021,15,1,2021), 15, msg= info)  
    def test_exemple_2(self):
        info = msg + "\nentre le 1/1/2021 et le 31/12/2021 il y a 365 jours"
        self.assertEqual(eleve.nb_jours(1,1,2021,31,12,2021), 365, msg= info)  
    def test_exemple_3(self):
        info = msg + "\nentre le 1/1/2024 et le 31/12/2024 il y a 366 jours"
        self.assertEqual(eleve.nb_jours(1,1,2024,31,12,2024), 366, msg= info)  
    def test_exemple_4(self):
        info = msg + "\nentre le 1/1/1970 et le 31/12/2021 il y a 18993 jours"
        self.assertEqual(eleve.nb_jours(1,1,1970,31,12,2021), 18993, msg= info)
    def test_alea(self):
        for _ in range(25):
            j_1, j_2 = randint(1, 28), randint(1, 28)
            m_1, m_2 = randint(1, 12), randint(1, 12)
            a_1 = randint(0, 3000)
            a_2 = a_1 + randint(0, 2000)
            rep_eleve = eleve.nb_jours(j_1, m_1, a_1, j_2, m_2, a_2)
            rep_prof  =  prof.nb_jours(j_1, m_1, a_1, j_2, m_2, a_2)
            info = msg + "\nentre le "
            info += str(j_1) + "/" + str(m_1) + "/" + str(a_1)
            info += " et le "
            info += str(j_2) + "/" + str(m_2) + "/" + str(a_2)
            info += " il y a " + str(rep_prof) + " jours."
            self.assertEqual(rep_eleve, rep_prof, msg=info)


  

        

if __name__ == '__main__':
    unittest.main()
