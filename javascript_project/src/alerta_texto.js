"use strict";

function textoAlerta(nivel, dias) {
  if (nivel === "rojo") return `Atención: tu dinero alcanza solo ${dias} días`;
  if (nivel === "amarillo") return "Precaución: tu dinero empieza a escasear pronto, revisa tus gastos";
  if (nivel === "verde") return "Vas bien: tu dinero alcanza por un buen tiempo";
  throw new RangeError(`Nivel de alerta desconocido: ${nivel}`);
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { textoAlerta };
}
