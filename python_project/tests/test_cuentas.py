import unittest

from src.cuentas import hash_contrasena, verificar_contrasena


class TestCuentas(unittest.TestCase):
    def test_el_hash_no_es_texto_plano_y_se_puede_verificar(self):
        almacenado = hash_contrasena("MiClave2026")
        self.assertNotIn("MiClave2026", almacenado)
        self.assertTrue(verificar_contrasena("MiClave2026", almacenado))
        self.assertFalse(verificar_contrasena("OtraClave999", almacenado))
