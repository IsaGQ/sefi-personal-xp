"""HU-04: mensaje con el día de quiebre ("¿en cuánto me quedo sin plata?")."""


def formatear_pesos(valor):
    """1200000 -> "$1.200.000".
    f"{valor:,.0f}" escribe el número sin decimales y con comas de miles
    ("1,200,000"); luego cambiamos las comas por puntos, como se usa en Colombia.
    """
    return "$" + f"{valor:,.0f}".replace(",", ".")


def mensaje_resultado(resultado):
    """Devuelve el texto que ve el usuario en la tarjeta de resultado."""
    if resultado.dia_quiebre is not None:
        return f"Te quedas sin dinero el día {resultado.dia_quiebre}"

    dias = len(resultado.saldos_diarios)
    saldo = formatear_pesos(resultado.saldo_final)
    return f"Tu dinero alcanza durante los {dias} días proyectados. Saldo final: {saldo}"