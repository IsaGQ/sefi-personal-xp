import unittest
from src.servicio import atender_solicitud_proyeccion

# Caso validado en Excel y en demo_cli.py: "Te quedas sin dinero el día 21"
PERFIL_DEMO = {
    "saldo_inicial": 500000,
    "ingreso_mensual": 0,
    "gastos_fijos_mensuales": 300000,
    "gasto_variable_diario_promedio": 15000,
    "dias_a_proyectar": 30,
}


class TestAtenderSolicitudProyeccion(unittest.TestCase):
    def test_datos_validos_responden_200_con_la_proyeccion(self):
        """HU-03 CA1 y CA2: usa el motor y coincide con Excel (quiebre el día 21)."""
        estado, cuerpo = atender_solicitud_proyeccion(PERFIL_DEMO)
        self.assertEqual(estado, 200)
        self.assertEqual(len(cuerpo["saldos_diarios"]), 30)
        self.assertEqual(cuerpo["dia_quiebre"], 21)
        self.assertEqual(cuerpo["saldo_final"], -250000)

    def test_datos_invalidos_responden_400_sin_detalles_tecnicos(self):
        """HU-03 CA3: error controlado, sin Traceback."""
        datos = dict(PERFIL_DEMO)
        datos["dias_a_proyectar"] = 0
        estado, cuerpo = atender_solicitud_proyeccion(datos)
        self.assertEqual(estado, 400)
        self.assertIn("dias_a_proyectar", cuerpo["errores"])
        self.assertNotIn("Traceback", str(cuerpo))

    def test_solicitud_incompleta_responde_400(self):
        """Excepciones: falta un campo (solicitud manipulada fuera del formulario)."""
        datos = dict(PERFIL_DEMO)
        del datos["ingreso_mensual"]
        estado, cuerpo = atender_solicitud_proyeccion(datos)
        self.assertEqual(estado, 400)
        self.assertIn("error", cuerpo)