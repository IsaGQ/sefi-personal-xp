"""HU-10: evaluación de una decisión de inversión o crédito con VAN y TIR."""
from __future__ import annotations

from typing import Sequence

from src.financial_engine import (
    DictamenFinanciero,
    FlujoInvalidoError,
    evaluar_viabilidad,
)

MAX_PERIODOS = 60


def evaluar_inversion(
    inversion_inicial: float, tasa_descuento: float, flujos: Sequence[float]
) -> DictamenFinanciero:
    """Arma [-I0, F1..Fn] y delega en el motor de decisión.

    Raises:
        FlujoInvalidoError: inversión <= 0 o cantidad de periodos fuera de 1..60.
    """
    if inversion_inicial <= 0:
        raise FlujoInvalidoError("La inversión inicial debe ser mayor que 0.")
    if not 1 <= len(flujos) <= MAX_PERIODOS:
        raise FlujoInvalidoError(f"Se admiten entre 1 y {MAX_PERIODOS} periodos.")
    return evaluar_viabilidad([-inversion_inicial, *flujos], tasa_descuento)
