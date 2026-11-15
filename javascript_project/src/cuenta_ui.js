"use strict";

function validarCorreo(correo) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(correo);
}

function validarContrasena(contrasena) {
  return contrasena.length >= 8;
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { validarCorreo, validarContrasena };
}
