import unittest

from src.financial_engine import FlujoInvalidoError
from src.variacion import calcular_variacion_porcentual


class TestCalcularVariacionPorcentual(unittest.TestCase):
    def test_variacion_de_reduccion_aumento_y_sin_cambio(self):
        """Hipótesis del proyecto: pasar de 100.000 a 80.000 es una reducción del 20 %."""
        self.assertEqual(calcular_variacion_porcentual(100_000, 80_000), -20.0)
        self.assertEqual(calcular_variacion_porcentual(100_000, 120_000), 20.0)
        self.assertEqual(calcular_variacion_porcentual(100_000, 100_000), 0.0)
        # Frontera: si el participante dejó de gastar por completo, la variación es -100 %.
        self.assertEqual(calcular_variacion_porcentual(100_000, 0), -100.0)

    def test_datos_invalidos_lanzan_excepcion(self):
        """Excepciones: el gasto inicial debe ser mayor que 0 y el final no puede ser negativo."""
        with self.assertRaises(FlujoInvalidoError):
            calcular_variacion_porcentual(0, 50_000)
        with self.assertRaises(FlujoInvalidoError):
            calcular_variacion_porcentual(-1, 50_000)
        with self.assertRaises(FlujoInvalidoError):
            calcular_variacion_porcentual(100_000, -1)