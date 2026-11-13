"""HU-04: mensaje con el día de quiebre."""


def mensaje_resultado(resultado):
    if resultado.dia_quiebre is not None:
        return "Te quedas sin dinero el día " + str(resultado.dia_quiebre)

    dias = len(resultado.saldos_diarios)
    saldo = f"{resultado.saldo_final:,.0f}".replace(",", ".")
    return "Tu dinero alcanza durante los " + str(dias) + " días proyectados. Saldo final: $" + saldo