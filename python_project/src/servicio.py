"""HU-03: el servicio web usa el motor financiero para proyectar el saldo.
Recibe los datos del formulario (un diccionario) y devuelve (código HTTP, respuesta).
"""

from .financial_engine import PerfilFinanciero, proyectar_saldo
from .validaciones import validar_datos_formulario

HTTP_OK = 200
HTTP_DATOS_INVALIDOS = 400
MENSAJE_ERROR = "Revisa los datos ingresados."


def _respuesta_error(errores):
    """Respuesta 400 con un mensaje para el usuario (nunca detalles técnicos)."""
    return HTTP_DATOS_INVALIDOS, {"error": MENSAJE_ERROR, "errores": errores}


def _crear_perfil(datos):
    """Convierte los datos del formulario en el PerfilFinanciero del motor."""
    return PerfilFinanciero(
        float(datos["saldo_inicial"]),
        float(datos["ingreso_mensual"]),
        float(datos["gastos_fijos_mensuales"]),
        float(datos["gasto_variable_diario_promedio"]),
        int(datos["dias_a_proyectar"]),
    )


def atender_solicitud_proyeccion(datos):
    """Valida los datos, llama al motor y arma la respuesta JSON."""
    try:
        errores = validar_datos_formulario(datos)
        if errores:
            return _respuesta_error(errores)
        resultado = proyectar_saldo(_crear_perfil(datos))
    except KeyError:  # falta un campo en la solicitud
        return _respuesta_error({})

    return HTTP_OK, {
        "saldos_diarios": resultado.saldos_diarios,
        "dia_quiebre": resultado.dia_quiebre,
        "saldo_final": resultado.saldo_final,
    }
    
    
