import unittest
from src.validaciones import validar_datos_formulario

DATOS_VALIDOS = {
    "saldo_inicial": "500000",
    "ingreso_mensual": "0",
    "gastos_fijos_mensuales": "300000",
    "gasto_variable_diario_promedio": "15000",
    "dias_a_proyectar": "30",
}


def con(campo, valor):
    """Copia de DATOS_VALIDOS cambiando un solo campo."""
    datos = dict(DATOS_VALIDOS)
    datos[campo] = valor
    return datos


class TestValidarDatosFormulario(unittest.TestCase):
    def test_datos_correctos_no_tienen_errores(self):
        """Regla de negocio: si todo está bien, el diccionario de errores queda vacío."""
        self.assertEqual(validar_datos_formulario(DATOS_VALIDOS), {})

    def test_texto_o_codigo_en_un_campo_numerico_se_rechaza(self):
            """HU-02 CA1 y CA4: letras o una etiqueta <script> no llegan al motor."""
            errores = validar_datos_formulario(con("saldo_inicial", "quinientos"))
            self.assertEqual(errores["saldo_inicial"], "Ingresa solo números")

            errores = validar_datos_formulario(con("ingreso_mensual", "<script>alert(1)</script>"))
            self.assertIn("ingreso_mensual", errores)
        

    def test_gasto_negativo_y_dias_en_el_limite(self):
            """HU-02 CA2 y valores frontera: 0 días falla, 1 día es válido."""
            errores = validar_datos_formulario(con("gasto_variable_diario_promedio", "-1"))
            self.assertEqual(
                errores["gasto_variable_diario_promedio"],
                "El gasto variable diario no puede ser negativo",
            )

            errores = validar_datos_formulario(con("dias_a_proyectar", "0"))
            self.assertEqual(
                errores["dias_a_proyectar"],
                "Los días a proyectar deben ser mayores que 0",
            )
            self.assertEqual(validar_datos_formulario(con("dias_a_proyectar", "1")), {})