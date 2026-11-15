"use strict";

function esUrlSegura(url) {
  return url.startsWith("https://");
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { esUrlSegura };
}
