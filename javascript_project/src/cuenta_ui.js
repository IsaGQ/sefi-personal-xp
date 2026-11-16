"use strict";

// HU-14: validaciones del formulario de cuenta (registro e inicio de sesión).
const FORMATO_CORREO = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
const LONGITUD_MINIMA = 8;

function validarCorreo(correo) {
  return FORMATO_CORREO.test(String(correo).trim());
}

function validarContrasena(contrasena) {
  return typeof contrasena === "string" && contrasena.length >= LONGITUD_MINIMA;
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { validarCorreo, validarContrasena };
}
