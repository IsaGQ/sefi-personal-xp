"use strict";

function formatearDictamen(mensaje) {
  if (mensaje.includes("Esta herramienta es informativa y no reemplaza la asesoría financiera profesional")) {
    return mensaje;
  }
  return mensaje + ". Esta herramienta es informativa y no reemplaza la asesoría financiera profesional.";
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { formatearDictamen };
}
