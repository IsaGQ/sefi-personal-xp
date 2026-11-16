import unittest
from datetime import datetime, timezone

from src.consentimiento import ConsentimientoRechazadoError, registrar_consentimiento


class TestConsentimiento(unittest.TestCase):
    def test_rechazo_lanza_error_y_aceptacion_guarda_solo_fecha_y_hora(self):
        with self.assertRaises(ConsentimientoRechazadoError):
            registrar_consentimiento(False)
        momento = datetime(2026, 11, 12, 10, 0, tzinfo=timezone.utc)
        registro = registrar_consentimiento(True, momento)
        self.assertEqual(registro, {"fecha_hora": "2026-11-12T10:00:00+00:00"})
