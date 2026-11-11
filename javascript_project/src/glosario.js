"use strict";

// HU-20: glosario en lenguaje sencillo.

const GLOSARIO = {
  "día de quiebre": "Es el día en que tu saldo se vuelve negativo si nada cambia.",
  "gasto hormiga": "Son los gastos pequeños y frecuentes (onces, transporte, antojos) que parecen insignificantes pero suman.",
  "van": "Valor Actual Neto: cuánto vale hoy lo que ganarías o perderías con una decisión. Si es positivo, conviene.",
  "tir": "Tasa Interna de Retorno: el rendimiento de una decisión expresado en porcentaje.",
};

function obtenerDefinicion(termino) {
  const clave = String(termino).trim().toLowerCase();
  if (!Object.hasOwn(GLOSARIO, clave)) {
    throw new Error(`El término «${termino}» no está en el glosario`);
  }
  return GLOSARIO[clave];
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { obtenerDefinicion };
}