"use strict";

// HU-20: glosario en lenguaje sencillo.

const GLOSARIO = Object.freeze({
  "día de quiebre": "Es el día en que tu saldo se vuelve negativo si nada cambia.",
  "gasto hormiga": "Son los gastos pequeños y frecuentes (onces, transporte, antojos) que parecen insignificantes pero suman.",
  "van": "Valor Actual Neto: cuánto vale hoy lo que ganarías o perderías con una decisión. Si es positivo, conviene.",
  "tir": "Tasa Interna de Retorno: el rendimiento de una decisión expresado en porcentaje.",
});

function normalizarTermino(termino) {
  return String(termino).trim().toLowerCase();
}

/**
 * Devuelve la definición en lenguaje sencillo de un término financiero (HU-20).
 * No distingue mayúsculas ni espacios al inicio o al final.
 * @param {string} termino Por ejemplo "VAN" o "gasto hormiga".
 * @returns {string} La definición.
 * @throws {Error} Si el término no está en el glosario.
 */
function obtenerDefinicion(termino) {
  const clave = normalizarTermino(termino);
  if (!Object.hasOwn(GLOSARIO, clave)) {
    throw new Error(`El término «${termino}» no está en el glosario`);
  }
  return GLOSARIO[clave];
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { obtenerDefinicion };
}