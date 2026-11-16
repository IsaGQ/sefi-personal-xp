const test = require("node:test");
const assert = require("node:assert/strict");
const { formatearDictamen } = require("../src/dictamen_ui.js");

test("HU-11: el dictamen termina con el aviso informativo", () => {
  const texto = formatearDictamen("Esta decisión sí te conviene");
  assert.ok(texto.includes("Esta herramienta es informativa"));
});

test("HU-11: no duplica el aviso si ya viene incluido", () => {
  const una = formatearDictamen("Hola");
  assert.equal(formatearDictamen(una), una);
});
