"use strict";

function parsearFlujos(texto) {
  const flujos = String(texto)
    .split(/[,;\n]/)
    .map((p) => p.trim())
    .filter((p) => p !== "")
    .map(Number);
  if (flujos.length < 1 || flujos.length > 60 || flujos.some(Number.isNaN)) {
    throw new RangeError("Ingresa entre 1 y 60 flujos numéricos");
  }
  return flujos;
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { parsearFlujos };
}
