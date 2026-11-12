"use strict";

// HU-01: separador de miles en los campos de dinero del formulario.
const SEPARADOR_MILES = ".";
const CIFRAS_POR_GRUPO = 3;

/** Quita los puntos que ya tenga el texto: "1.500.000" -> "1500000". */
function quitarPuntos(texto) {
  return String(texto).split(SEPARADOR_MILES).join("");
}


function formatearMiles(valor) {
  const digitos = quitarPuntos(valor);
  let resultado = "";

  for (let i = 0; i < digitos.length; i++) {
    const cifrasQueFaltan = digitos.length - i;
    const empiezaUnGrupo = i > 0 && cifrasQueFaltan % CIFRAS_POR_GRUPO === 0;

    if (empiezaUnGrupo) {
      resultado += SEPARADOR_MILES;
    }

    resultado += digitos[i];
  }

  return resultado;
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { formatearMiles };
}