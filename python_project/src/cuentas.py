import hashlib
import os


def hash_contrasena(contrasena):
    sal = os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", contrasena.encode("utf-8"), sal, 200_000)
    return f"{sal.hex()}${digest.hex()}"


def verificar_contrasena(contrasena, almacenado):
    sal_hex, hash_hex = almacenado.split("$")
    digest = hashlib.pbkdf2_hmac("sha256", contrasena.encode("utf-8"), bytes.fromhex(sal_hex), 200_000)
    return digest.hex() == hash_hex
