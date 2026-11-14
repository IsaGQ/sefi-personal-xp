MSG_SOLO_NUMEROS = "Ingresa solo números"
MSG_GASTO_NEGATIVO = "El gasto variable diario no puede ser negativo"
MSG_DIAS_INVALIDOS = "Los días a proyectar deben ser mayores que 0"


def _es_numero(valor):
    """True si el valor se puede convertir a número ("15000" sí, "abc" no)."""
    try:
        float(valor)
        return True
    except (ValueError, TypeError):
        return False


def validar_datos_formulario(datos):
    """Revisa los datos del formulario y devuelve {campo: mensaje de error}.
    Si el diccionario que devuelve está vacío, los datos son válidos.
    """
    errores = {}

    for campo in datos:
        if not _es_numero(datos[campo]):
            errores[campo] = MSG_SOLO_NUMEROS

    gasto = "gasto_variable_diario_promedio"
    if gasto not in errores and float(datos[gasto]) < 0:
        errores[gasto] = MSG_GASTO_NEGATIVO

    dias = "dias_a_proyectar"
    if dias not in errores and float(datos[dias]) <= 0:
        errores[dias] = MSG_DIAS_INVALIDOS

    return errores