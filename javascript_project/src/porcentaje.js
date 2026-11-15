"use strict";

function validarPorcentaje(valor) {
  const numero = Number(valor);
  if (valor === "" || Number.isNaN(numero) || numero < 0 || numero > 100) {
    throw new RangeError("El porcentaje debe estar entre 0 y 100");
  }
  return numero / 100;
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { validarPorcentaje };
}
