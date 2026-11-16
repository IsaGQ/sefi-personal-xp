import unittest

from src.anonimizar import anonimizar_participante
from src.financial_engine import FlujoInvalidoError


class TestAnonimizarParticipante(unittest.TestCase):
    def test_elimina_identificadores_y_asigna_codigo_sin_modificar_el_original(self):
        """Ley 1581: el conjunto de análisis no debe tener nombre ni correo."""
        original = {"nombre": "Ana Pérez", "correo": "ana@correo.com", "gasto_inicial": 100_000, "gasto_final": 80_000}
        anonimo = anonimizar_participante(original, 7)
        self.assertEqual(anonimo, {"codigo": "P-007", "gasto_inicial": 100_000, "gasto_final": 80_000})
        # El diccionario original no se modifica.
        self.assertIn("nombre", original)

    def test_entradas_invalidas_lanzan_excepcion(self):
        """Excepciones: número de participante inválido o participante que no es un diccionario."""
        participante = {"nombre": "Ana", "correo": "ana@correo.com"}
        for numero_invalido in (0, -1, "7", True):
            with self.subTest(numero=numero_invalido):
                with self.assertRaises(FlujoInvalidoError):
                    anonimizar_participante(participante, numero_invalido)
        with self.assertRaises(FlujoInvalidoError):
            anonimizar_participante(None, 1)