"use strict";

/**
 * HU-12: el portal solo continúa si el usuario aceptó el aviso de privacidad.
 * Se compara con `true` estricto para que valores como "false", 1 o undefined no cuenten.
 * @param {unknown} aceptado
 * @returns {boolean}
 */
function puedeContinuar(aceptado) {
  return aceptado === true;
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { puedeContinuar };
}
