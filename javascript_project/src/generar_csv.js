"use strict";

// HU-18: exportación de la proyección a un archivo CSV.

function generarCSV(saldos) {
  if (!Array.isArray(saldos) || saldos.length === 0) {
    throw new Error("Se requiere al menos un saldo para exportar");
  }
  if (!saldos.every(Number.isFinite)) {
    throw new TypeError("Todos los saldos deben ser números");
  }
  const filas = saldos.map((saldo, indice) => `${indice + 1},${saldo}`);
  return ["dia,saldo", ...filas].join("\n");
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { generarCSV };
}