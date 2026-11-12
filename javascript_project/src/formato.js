"use strict";

// HU-01: separador de miles en los campos de dinero del formulario.
function formatearMiles(valor) {
  const digitos = String(valor).split(".").join("");
  let resultado = "";

  for (let i = 0; i < digitos.length; i++) {
    const faltan = digitos.length - i;

    if (i > 0 && faltan % 3 === 0) {
      resultado = resultado + ".";
    }

    resultado = resultado + digitos[i];
  }

  return resultado;
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { formatearMiles };
}