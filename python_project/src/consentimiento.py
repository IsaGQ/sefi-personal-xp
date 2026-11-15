"""HU-12: consentimiento informado (Ley 1581 de 2012). Solo se guarda fecha y hora."""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Dict, Optional


class ConsentimientoRechazadoError(Exception):
    """El usuario no aceptó el aviso de privacidad: no se almacena nada."""


def registrar_consentimiento(acepta: bool, ahora: Optional[datetime] = None) -> Dict[str, str]:
    """Registra el consentimiento sin datos identificables (minimización)."""
    if not acepta:
        raise ConsentimientoRechazadoError("Sin consentimiento no se puede usar el portal.")
    momento = ahora or datetime.now(timezone.utc)
    return {"fecha_hora": momento.isoformat()}
