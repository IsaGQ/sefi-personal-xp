"use strict";

// HU-09: valida el porcentaje de reducción del gasto hormiga y lo devuelve como fracción.
const MIN = 0;
const MAX = 100;

function esPorcentajeValido(valor) {
  if (valor === "" || valor === null || valor === undefined) return false;
  const numero = Number(valor);
  return !Number.isNaN(numero) && numero >= MIN && numero <= MAX;
}

function validarPorcentaje(valor) {
  if (!esPorcentajeValido(valor)) {
    throw new RangeError(`El porcentaje debe estar entre ${MIN} y ${MAX}`);
  }
  return Number(valor) / 100;
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { validarPorcentaje };
}
