import unittest

from src.financial_engine import FlujoInvalidoError
from src.gasto_diario import estimar_gasto_diario


class TestEstimarGastoDiario(unittest.TestCase):
    def test_promedio_diario_es_el_total_semanal_entre_siete(self):
        """Lógica algorítmica: (14.000 + 28.000 + 7.000) / 7 = 7.000 por día."""
        gastos = {"onces": 14_000, "transporte": 28_000, "antojos": 7_000}
        self.assertEqual(estimar_gasto_diario(gastos), 7_000)
        # Valor frontera: exactamente 10 categorías sigue siendo válido.
        diez = {f"categoria_{i}": 7_000 for i in range(10)}
        self.assertEqual(estimar_gasto_diario(diez), 10_000)

    def test_entradas_invalidas_lanzan_excepcion(self):
        """Excepciones: sin categorías, monto negativo o más de 10 categorías."""
        with self.assertRaises(FlujoInvalidoError):
            estimar_gasto_diario({})
        with self.assertRaises(FlujoInvalidoError):
            estimar_gasto_diario({"onces": -1})
        once = {f"categoria_{i}": 1_000 for i in range(11)}
        with self.assertRaises(FlujoInvalidoError):
            estimar_gasto_diario(once)