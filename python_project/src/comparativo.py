"""HU-09: comparación entre la proyección actual y una con menos gasto hormiga."""
from __future__ import annotations

from typing import Optional, TypedDict

from src.financial_engine import (
    FlujoInvalidoError,
    PerfilFinanciero,
    proyectar_saldo,
    simular_reduccion_gasto_hormiga,
)

DIAS_POR_MES = 30


class ResumenComparativo(TypedDict):
    dias_ganados: Optional[int]  # None si falta alguno de los dos días de quiebre
    saldo_final_adicional: float
    ahorro_mensual: float


def resumen_comparativo(
    perfil: PerfilFinanciero, porcentaje_reduccion: float = 0.20
) -> ResumenComparativo:
    """Compara el escenario base con el reducido (por defecto, 20 %)."""
    if perfil is None:
        raise FlujoInvalidoError("El perfil financiero no puede ser nulo.")
    base = proyectar_saldo(perfil)
    reducido = simular_reduccion_gasto_hormiga(perfil, porcentaje_reduccion)

    if base.dia_quiebre is None or reducido.dia_quiebre is None:
        dias_ganados = None
    else:
        dias_ganados = reducido.dia_quiebre - base.dia_quiebre

    ahorro = perfil.gasto_variable_diario_promedio * porcentaje_reduccion * DIAS_POR_MES
    return {
        "dias_ganados": dias_ganados,
        "saldo_final_adicional": round(reducido.saldo_final - base.saldo_final, 2),
        "ahorro_mensual": round(ahorro, 2),
    }
