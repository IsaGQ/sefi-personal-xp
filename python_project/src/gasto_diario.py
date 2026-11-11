"""HU-15: estimador del gasto hormiga diario a partir de gastos semanales por categoría."""
from __future__ import annotations

from typing import Dict

from .financial_engine import FlujoInvalidoError

DIAS_POR_SEMANA = 7
MAX_CATEGORIAS_GASTO = 10


def _validar_gastos_semanales(gastos_semanales: Dict[str, float]) -> None:
    """Verifica las reglas de HU-15: al menos 1 y máximo 10 categorías, sin negativos."""
    if not gastos_semanales:
        raise FlujoInvalidoError("Debes registrar al menos una categoría de gasto.")
    if len(gastos_semanales) > MAX_CATEGORIAS_GASTO:
        raise FlujoInvalidoError(f"Máximo {MAX_CATEGORIAS_GASTO} categorías de gasto.")
    if any(monto < 0 for monto in gastos_semanales.values()):
        raise FlujoInvalidoError("Los montos no pueden ser negativos.")


def estimar_gasto_diario(gastos_semanales: Dict[str, float]) -> float:
    """Convierte los gastos semanales por categoría en un promedio diario (HU-15).

    Args:
        gastos_semanales: Diccionario {categoría: monto gastado en una semana}.

    Returns:
        El gasto variable diario promedio (total semanal dividido entre 7).

    Raises:
        FlujoInvalidoError: si no hay categorías, hay más de 10 o algún monto es negativo.
    """
    _validar_gastos_semanales(gastos_semanales)
    return round(sum(gastos_semanales.values()) / DIAS_POR_SEMANA, 2)