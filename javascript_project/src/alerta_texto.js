"use strict";

// HU-08: textos de la alerta tipo semáforo.
const TEXTOS = {
  rojo: (dias) => `Atención: tu dinero alcanza solo ${dias} días`,
  amarillo: () => "Precaución: tu dinero empieza a escasear pronto, revisa tus gastos",
  verde: () => "Vas bien: tu dinero alcanza por un buen tiempo",
};

function textoAlerta(nivel, dias) {
  if (!Object.hasOwn(TEXTOS, nivel)) {
    throw new RangeError(`Nivel de alerta desconocido: ${nivel}`);
  }
  return TEXTOS[nivel](dias);
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { textoAlerta };
}
