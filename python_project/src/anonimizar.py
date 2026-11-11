"""HU-17: anonimización de los datos de los participantes del experimento (Ley 1581 de 2012)."""
from __future__ import annotations

from typing import Any, Dict

from .financial_engine import FlujoInvalidoError

IDENTIFICADORES_DIRECTOS = ("nombre", "correo")


def _codigo_participante(numero: int) -> str:
    """Código anónimo con 3 dígitos, por ejemplo P-007."""
    if isinstance(numero, bool) or not isinstance(numero, int) or numero < 1:
        raise FlujoInvalidoError("El número de participante debe ser un entero mayor que 0.")
    return f"P-{numero:03d}"


def anonimizar_participante(participante: Dict[str, Any], numero: int) -> Dict[str, Any]:
    """Quita los identificadores directos de un participante y le asigna un código (HU-17).

    No modifica el diccionario recibido: devuelve uno nuevo.

    Raises:
        FlujoInvalidoError: si el participante no es un diccionario o el número no es un entero mayor que 0.
    """
    if not isinstance(participante, dict):
        raise FlujoInvalidoError("El participante debe ser un diccionario.")
    anonimo = {
        clave: valor for clave, valor in participante.items() if clave not in IDENTIFICADORES_DIRECTOS
    }
    anonimo["codigo"] = _codigo_participante(numero)
    return anonimo