import unittest

from src.alertas import clasificar_alerta


class TestClasificarAlerta(unittest.TestCase):
    def test_semaforo_rojo_amarillo_y_verde(self):
        self.assertEqual(clasificar_alerta(15), "rojo")
        self.assertEqual(clasificar_alerta(16), "amarillo")
        self.assertEqual(clasificar_alerta(30), "amarillo")
        self.assertEqual(clasificar_alerta(31), "verde")
        self.assertEqual(clasificar_alerta(None), "verde")
