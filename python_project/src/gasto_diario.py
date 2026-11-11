"""HU-15: estimador del gasto hormiga diario a partir de gastos semanales por categoría."""
from __future__ import annotations

from typing import Dict

from .financial_engine import FlujoInvalidoError


def estimar_gasto_diario(gastos_semanales: Dict[str, float]) -> float:
    if not gastos_semanales:
        raise FlujoInvalidoError("Debes registrar al menos una categoría de gasto.")
    if len(gastos_semanales) > 10:
        raise FlujoInvalidoError("Máximo 10 categorías de gasto.")
    if any(monto < 0 for monto in gastos_semanales.values()):
        raise FlujoInvalidoError("Los montos no pueden ser negativos.")
    return round(sum(gastos_semanales.values()) / 7, 2)