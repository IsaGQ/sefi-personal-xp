import unittest
from src.financial_engine import PerfilFinanciero, ResultadoProyeccion, proyectar_saldo
from src.mensajes import mensaje_resultado


class TestMensajeResultado(unittest.TestCase):
    def test_con_dia_de_quiebre_dice_el_dia(self):
        """HU-04 CA1 y CA3: mismo día que el motor y que Excel (día 21)."""
        resultado = proyectar_saldo(PerfilFinanciero(500000, 0, 300000, 15000, 30))
        self.assertEqual(mensaje_resultado(resultado), "Te quedas sin dinero el día 21")

    def test_sin_quiebre_dice_que_alcanza_y_el_saldo_final(self):
        """HU-04 CA2: mensaje positivo con los días y el saldo final con puntos de miles."""
        resultado = ResultadoProyeccion(saldos_diarios=[1200000.0] * 60, dia_quiebre=None)
        self.assertEqual(
            mensaje_resultado(resultado),
            "Tu dinero alcanza durante los 60 días proyectados. Saldo final: $1.200.000",
        )