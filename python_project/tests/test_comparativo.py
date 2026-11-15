import unittest

from src.comparativo import resumen_comparativo
from src.financial_engine import PerfilFinanciero


class TestResumenComparativo(unittest.TestCase):
    def test_reducir_20_por_ciento_gana_dias_y_ahorra(self):
        # Caso demo: sin reducción se queda sin dinero el día 21
        perfil = PerfilFinanciero(500_000, 0, 300_000, 15_000, 30)
        resumen = resumen_comparativo(perfil)
        self.assertGreater(resumen["dias_ganados"], 0)
        self.assertEqual(resumen["ahorro_mensual"], 90_000)
