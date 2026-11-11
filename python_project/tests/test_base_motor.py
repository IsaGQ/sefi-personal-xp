import unittest

from src.financial_engine import PerfilFinanciero, proyectar_saldo


class TestMotorExistente(unittest.TestCase):
    def test_prueba_base_dia_de_quiebre_del_caso_demo(self):
        """Prueba base (humo): confirma que el motor de la Etapa 1 funciona dentro del nuevo repositorio."""
        perfil = PerfilFinanciero(500_000, 0, 300_000, 15_000, 30)
        self.assertEqual(proyectar_saldo(perfil).dia_quiebre, 21)
