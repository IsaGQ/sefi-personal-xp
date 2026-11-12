"""HU-03: el servicio web usa el motor financiero para proyectar el saldo."""

from .financial_engine import PerfilFinanciero, proyectar_saldo
from .validaciones import validar_datos_formulario


def atender_solicitud_proyeccion(datos):
    try:
        errores = validar_datos_formulario(datos)
        if errores:
            return 400, {"error": "Revisa los datos ingresados.", "errores": errores}

        perfil = PerfilFinanciero(
            float(datos["saldo_inicial"]),
            float(datos["ingreso_mensual"]),
            float(datos["gastos_fijos_mensuales"]),
            float(datos["gasto_variable_diario_promedio"]),
            int(datos["dias_a_proyectar"]),
        )
        resultado = proyectar_saldo(perfil)
    except KeyError:
        return 400, {"error": "Revisa los datos ingresados.", "errores": {}}

    return 200, {
        "saldos_diarios": resultado.saldos_diarios,
        "dia_quiebre": resultado.dia_quiebre,
        "saldo_final": resultado.saldo_final,
    }
    
    
