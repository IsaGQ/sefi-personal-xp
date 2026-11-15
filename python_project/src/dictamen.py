"""HU-11: dictamen de viabilidad en lenguaje sencillo."""
from __future__ import annotations

from src.financial_engine import DictamenFinanciero, EvaluacionTIR, EvaluacionVAN

AVISO = "Esta herramienta es informativa y no reemplaza la asesoría financiera profesional"


def _titulo(dictamen: DictamenFinanciero) -> str:
    van_ok = dictamen.evaluacion_van == EvaluacionVAN.VIABLE
    tir_ok = dictamen.evaluacion_tir == EvaluacionTIR.ACEPTABLE
    if van_ok and tir_ok:
        return "Esta decisión sí te conviene"
    if dictamen.evaluacion_van == EvaluacionVAN.NO_VIABLE and not tir_ok:
        return "Esta decisión no es recomendable"
    return "Esta decisión está en el límite: revisa los números con calma"


def mensaje_dictamen(dictamen: DictamenFinanciero) -> str:
    """Traduce VAN y TIR a una frase comprensible, con el aviso legal."""
    return f"{_titulo(dictamen)}. {AVISO}."
