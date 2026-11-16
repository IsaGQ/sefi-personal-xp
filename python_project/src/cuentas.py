"""HU-14: contraseñas seguras (sal + PBKDF2); nunca se guardan en texto plano."""
from __future__ import annotations

import hashlib
import hmac
import os
from typing import Optional

from src.financial_engine import FlujoInvalidoError

LONGITUD_MINIMA = 8
ITERACIONES = 200_000


def validar_contrasena(contrasena: str) -> bool:
    """True si tiene al menos 8 caracteres; lanza error si no es texto."""
    if not isinstance(contrasena, str):
        raise FlujoInvalidoError("La contraseña debe ser texto.")
    return len(contrasena) >= LONGITUD_MINIMA


def _derivar(contrasena: str, sal: bytes) -> str:
    return hashlib.pbkdf2_hmac("sha256", contrasena.encode("utf-8"), sal, ITERACIONES).hex()


def hash_contrasena(contrasena: str, sal: Optional[bytes] = None) -> str:
    """Devuelve 'sal$hash' en hexadecimal."""
    if not validar_contrasena(contrasena):
        raise FlujoInvalidoError(f"La contraseña debe tener al menos {LONGITUD_MINIMA} caracteres.")
    sal = sal or os.urandom(16)
    return f"{sal.hex()}${_derivar(contrasena, sal)}"


def verificar_contrasena(contrasena: str, almacenado: str) -> bool:
    """Compara en tiempo constante la contraseña contra el hash almacenado."""
    try:
        sal_hex, hash_hex = almacenado.split("$")
        esperado = _derivar(contrasena, bytes.fromhex(sal_hex))
    except (ValueError, AttributeError):
        return False
    return hmac.compare_digest(esperado, hash_hex)
