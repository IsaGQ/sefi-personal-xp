"""HU-17: anonimización de los datos de los participantes del experimento (Ley 1581 de 2012)."""
from __future__ import annotations

from typing import Any, Dict

from .financial_engine import FlujoInvalidoError


def anonimizar_participante(participante: Dict[str, Any], numero: int) -> Dict[str, Any]:
    if not isinstance(participante, dict):
        raise FlujoInvalidoError("El participante debe ser un diccionario.")
    if isinstance(numero, bool) or not isinstance(numero, int) or numero < 1:
        raise FlujoInvalidoError("El número de participante debe ser un entero mayor que 0.")
    anonimo = {clave: valor for clave, valor in participante.items() if clave not in ("nombre", "correo")}
    anonimo["codigo"] = f"P-{numero:03d}"
    return anonimo