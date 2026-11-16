"use strict";

// HU-13: verifica que una dirección use HTTPS (cifrado en tránsito).
function esUrlSegura(url) {
  try {
    return new URL(url).protocol === "https:";
  } catch {
    return false;
  }
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { esUrlSegura };
}
