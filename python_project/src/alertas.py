"""HU-08: alerta preventiva tipo semáforo según qué tan cerca está el día de quiebre."""
from __future__ import annotations

from typing import Optional

from src.financial_engine import FlujoInvalidoError

UMBRAL_ROJO = 15       # rojo: faltan 15 días o menos
UMBRAL_AMARILLO = 30   # amarillo: entre 16 y 30 días


def clasificar_alerta(
    dia_quiebre: Optional[int],
    umbral_rojo: int = UMBRAL_ROJO,
    umbral_amarillo: int = UMBRAL_AMARILLO,
) -> str:
    """Devuelve 'rojo', 'amarillo' o 'verde' según el día de quiebre.

    Raises:
        FlujoInvalidoError: si el día de quiebre es menor que 1.
    """
    if dia_quiebre is None:
        return "verde"
    if dia_quiebre < 1:
        raise FlujoInvalidoError("El día de quiebre debe ser mayor o igual a 1.")
    if dia_quiebre <= umbral_rojo:
        return "rojo"
    if dia_quiebre <= umbral_amarillo:
        return "amarillo"
    return "verde"
