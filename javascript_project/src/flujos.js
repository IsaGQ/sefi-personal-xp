"use strict";

// HU-10: convierte el texto de flujos de caja del usuario en una lista de números.
const MAX_PERIODOS = 60;
const SEPARADORES = /[,;\n]/;

function parsearFlujos(texto) {
  const flujos = String(texto)
    .split(SEPARADORES)
    .map((parte) => parte.trim())
    .filter((parte) => parte !== "")
    .map(Number);
  const cantidadValida = flujos.length >= 1 && flujos.length <= MAX_PERIODOS;
  if (!cantidadValida || flujos.some(Number.isNaN)) {
    throw new RangeError(`Ingresa entre 1 y ${MAX_PERIODOS} flujos numéricos`);
  }
  return flujos;
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { parsearFlujos };
}
