def validar_datos_formulario(datos):
    errores = {}

    for campo in datos:
        try:
            float(datos[campo])
        except (ValueError, TypeError):
            errores[campo] = "Ingresa solo números"

    gasto = "gasto_variable_diario_promedio"
    if gasto not in errores and float(datos[gasto]) < 0:
        errores[gasto] = "El gasto variable diario no puede ser negativo"

    dias = "dias_a_proyectar"
    if dias not in errores and float(datos[dias]) <= 0:
        errores[dias] = "Los días a proyectar deben ser mayores que 0"

    return errores