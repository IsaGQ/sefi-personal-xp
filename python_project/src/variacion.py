"""HU-16: variación porcentual del gasto hormiga entre la medición inicial y la final."""
from __future__ import annotations

from .financial_engine import FlujoInvalidoError


def calcular_variacion_porcentual(gasto_inicial: float, gasto_final: float) -> float:
    if gasto_inicial <= 0 or gasto_final < 0:
        raise FlujoInvalidoError("El gasto inicial debe ser mayor que 0 y el final no puede ser negativo.")
    return round((gasto_final - gasto_inicial) / gasto_inicial * 100, 2)