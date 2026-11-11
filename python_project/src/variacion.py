"""HU-16: variación porcentual del gasto hormiga entre la medición inicial y la final."""
from __future__ import annotations

from .financial_engine import FlujoInvalidoError

FACTOR_PORCENTAJE = 100


def calcular_variacion_porcentual(gasto_inicial: float, gasto_final: float) -> float:
    """Calcula en qué porcentaje cambió el gasto hormiga de un participante (HU-16).

    Un resultado negativo es una reducción (por ejemplo, -20.0 significa que gastó 20 % menos).

    Raises:
        FlujoInvalidoError: si el gasto inicial no es mayor que 0 o el final es negativo.
    """
    if gasto_inicial <= 0:
        raise FlujoInvalidoError("El gasto inicial debe ser mayor que 0.")
    if gasto_final < 0:
        raise FlujoInvalidoError("El gasto final no puede ser negativo.")
    cambio = gasto_final - gasto_inicial
    return round(cambio / gasto_inicial * FACTOR_PORCENTAJE, 2)