from src.financial_engine import evaluar_viabilidad


def evaluar_inversion(inversion_inicial, tasa_descuento, flujos):
    return evaluar_viabilidad([-inversion_inicial, *flujos], tasa_descuento)
