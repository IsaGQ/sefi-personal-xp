"use strict";

// HU-18: exportación de la proyección a un archivo CSV.

const ENCABEZADO_CSV = "dia,saldo";

function validarSaldos(saldos) {
  if (!Array.isArray(saldos) || saldos.length === 0) {
    throw new Error("Se requiere al menos un saldo para exportar");
  }
  if (!saldos.every(Number.isFinite)) {
    throw new TypeError("Todos los saldos deben ser números");
  }
}

/**
 * Convierte la serie de saldos en texto CSV que abre Excel (HU-18).
 * @param {number[]} saldos Saldo de cada día proyectado (el primer elemento es el día 1).
 * @returns {string} Texto con el encabezado "dia,saldo" y una fila por día.
 * @throws {Error} Si la lista está vacía o contiene valores que no son números.
 */
function generarCSV(saldos) {
  validarSaldos(saldos);
  const filas = saldos.map((saldo, indice) => `${indice + 1},${saldo}`);
  return [ENCABEZADO_CSV, ...filas].join("\n");
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { generarCSV };
}