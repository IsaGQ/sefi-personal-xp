import unittest

from src.inversion import evaluar_inversion


class TestEvaluarInversion(unittest.TestCase):
    def test_van_y_tir_de_una_inversion_rentable(self):
        # -1000 hoy, +600 y +600 en dos periodos, r = 10 %
        d = evaluar_inversion(1000, 0.10, [600, 600])
        self.assertAlmostEqual(d.van, 41.32, places=2)
        self.assertAlmostEqual(d.tir, 0.1307, places=3)
