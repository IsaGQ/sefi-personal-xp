"use strict";

function puedeContinuar(aceptado) {
  return aceptado === true;
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { puedeContinuar };
}
