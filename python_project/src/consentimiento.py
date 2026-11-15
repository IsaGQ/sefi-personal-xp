class ConsentimientoRechazadoError(Exception):
    pass


def registrar_consentimiento(acepta, ahora=None):
    if not acepta:
        raise ConsentimientoRechazadoError("Sin consentimiento no se puede usar el portal.")
    return {"fecha_hora": ahora.isoformat()}
