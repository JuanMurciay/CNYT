
import unittest
import math

class TestlibrarycMethods(unittest.TestCase):

    def test_suma(self):
        suma = lc.suma((4, -1), (6, -5))
        self.assertAlmostEqual(suma[0], 10)
        self.assertAlmostEqual(suma[1], -6)

        suma2 = lc.suma((1, -8), (3, 2))
        self.assertAlmostEqual(suma2[0], 4)
        self.assertAlmostEqual(suma2[1], -6)

    def test_producto(self):
        producto = lc.producto((4, -1), (6, -5))
        self.assertAlmostEqual(producto[0], 19)
        self.assertAlmostEqual(producto[1], -26)

        producto2 = lc.producto((1, -8), (3, 2))
        self.assertAlmostEqual(producto2[0], 19)
        self.assertAlmostEqual(producto2[1], -22)

    def test_resta(self):
        resta = lc.resta((4, -1), (6, -5))
        self.assertAlmostEqual(resta[0], -2)
        self.assertAlmostEqual(resta[1], 4)

        resta2 = lc.resta((1, -8), (3, 2))
        self.assertAlmostEqual(resta2[0], -2)
        self.assertAlmostEqual(resta2[1], -10)

    def test_division(self):
        division = lc.division((4, -1), (6, -5))
        self.assertAlmostEqual(division[0], 0.0196078431372549)
        self.assertAlmostEqual(division[1], 0.7254901960784313)

        division2 = lc.division((1, -8), (3, 2))
        self.assertAlmostEqual(division2[0], -1.9)
        self.assertAlmostEqual(division2[1], -2.6)

    def test_modulo1(self):
        modulo = lc.modulo1((4, -2))
        self.assertAlmostEqual(modulo, 4.47213595499958)


    def test_conjugado(self):
        conjugado = lc.conjugado((4, -2))
        self.assertEqual(conjugado, (4, 2))

        conjugado2 = lc.conjugado((-1, 7))
        self.assertEqual(conjugado2, (-1, -7))

    def test_polarAcartesiano(self):
        polar1 = lc.polarAcartesiano((4, math.pi/5))
        self.assertAlmostEqual(polar1[0], 3.23606797749979)
        self.assertAlmostEqual(polar1[1], 2.3511410091698925)

        polar2 = lc.polarAcartesiano((2, math.pi/2))
        self.assertAlmostEqual(polar2[0], 1.2246467991473532e-16)
        self.assertAlmostEqual(polar2[1], 2.0)

    def test_cartesianoApolar(self):
        polar1 = lc.cartesianoApolar((4, -2))
        self.assertAlmostEqual(polar1[0], 4.47213595499958)
        self.assertAlmostEqual(polar1[1], math.atan2(-2, 4))

        polar2 = lc.cartesianoApolar((-1, 7))
        self.assertAlmostEqual(polar2[0], 7.0710678118654755)
        self.assertAlmostEqual(polar2[1], math.atan2(7, -1))

    def test_fase(self):
        fase1 = lc.fase((4, -2))
        self.assertAlmostEqual(fase1, math.atan2(-2, 4))

        fase2 = lc.fase((-1, 7))
        self.assertAlmostEqual(fase2, math.atan2(7, -1))

if __name__ == '__main__':
    unittest.main()
