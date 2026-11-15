def clasificar_alerta(dia_quiebre):
    if dia_quiebre is None or dia_quiebre > 30:
        return "verde"
    if dia_quiebre <= 15:
        return "rojo"
    return "amarillo"
