const test = require("node:test");
const assert = require("node:assert/strict");
const { textoAlerta } = require("../src/alerta_texto.js");

test("HU-08: la alerta roja indica los días que alcanza el dinero", () => {
  assert.equal(textoAlerta("rojo", 12), "Atención: tu dinero alcanza solo 12 días");
});

test("HU-08: un nivel desconocido lanza error", () => {
  assert.throws(() => textoAlerta("azul", 5), RangeError);
});
