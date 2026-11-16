"use strict";

// HU-11: agrega al dictamen el aviso de que no reemplaza la asesoría profesional.
const AVISO = "Esta herramienta es informativa y no reemplaza la asesoría financiera profesional";

function formatearDictamen(mensaje) {
  const texto = String(mensaje).trim();
  return texto.includes(AVISO) ? texto : `${texto}. ${AVISO}.`;
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { formatearDictamen, AVISO };
}
