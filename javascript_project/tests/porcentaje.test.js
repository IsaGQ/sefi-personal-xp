const test = require("node:test");
const assert = require("node:assert/strict");
const { validarPorcentaje } = require("../src/porcentaje.js");

test("HU-09: el porcentaje 20 se convierte en la fracción 0.2", () => {
  assert.equal(validarPorcentaje("20"), 0.2);
});

test("HU-09: vacío, no numérico o fuera de 0-100 se rechaza", () => {
  assert.throws(() => validarPorcentaje(""), RangeError);
  assert.throws(() => validarPorcentaje("abc"), RangeError);
  assert.throws(() => validarPorcentaje("101"), RangeError);
  assert.throws(() => validarPorcentaje("-1"), RangeError);
});
