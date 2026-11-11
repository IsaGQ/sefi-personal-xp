const test = require("node:test");
const assert = require("node:assert/strict");

test("prueba base: el módulo del cliente se puede cargar", () => {
  assert.equal(typeof require("../src/sefi_front.js"), "object");
});
