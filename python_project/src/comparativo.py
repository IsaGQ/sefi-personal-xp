from src.financial_engine import proyectar_saldo, simular_reduccion_gasto_hormiga


def resumen_comparativo(perfil, porcentaje_reduccion=0.20):
    base = proyectar_saldo(perfil)
    reducido = simular_reduccion_gasto_hormiga(perfil, porcentaje_reduccion)
    return {
        "dias_ganados": reducido.dia_quiebre - base.dia_quiebre,
        "ahorro_mensual": round(perfil.gasto_variable_diario_promedio * porcentaje_reduccion * 30, 2),
    }
