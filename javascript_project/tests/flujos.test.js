const test = require("node:test");
const assert = require("node:assert/strict");
const { parsearFlujos } = require("../src/flujos.js");

test("HU-10: separa flujos por coma, punto y coma o salto de línea", () => {
  assert.deepEqual(parsearFlujos("500, 600;700\n800"), [500, 600, 700, 800]);
});

test("HU-10: texto vacío o no numérico se rechaza", () => {
  assert.throws(() => parsearFlujos(""), RangeError);
  assert.throws(() => parsearFlujos("500, abc"), RangeError);
});

test("HU-10: más de 60 periodos se rechaza", () => {
  assert.throws(() => parsearFlujos(new Array(61).fill("1").join(",")), RangeError);
});
