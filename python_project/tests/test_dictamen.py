import unittest

from src.dictamen import AVISO, mensaje_dictamen
from src.inversion import evaluar_inversion


class TestMensajeDictamen(unittest.TestCase):
    def test_mensaje_segun_viabilidad_e_incluye_el_aviso(self):
        bueno = mensaje_dictamen(evaluar_inversion(1000, 0.10, [600, 600]))
        malo = mensaje_dictamen(evaluar_inversion(1000, 0.10, [300, 300]))
        self.assertIn("sí te conviene", bueno)
        self.assertIn("no es recomendable", malo)
        self.assertIn(AVISO, bueno)
        self.assertIn(AVISO, malo)
