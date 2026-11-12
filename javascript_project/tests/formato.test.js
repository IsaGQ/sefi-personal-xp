const test = require("node:test");
const assert = require("node:assert/strict");
const { formatearMiles } = require("../src/formato.js");

test("formatearMiles pone los puntos de miles (HU-01 CA3)", () => {
  assert.equal(formatearMiles(1500000), "1.500.000");
  assert.equal(formatearMiles("250000"), "250.000");
});

test("formatearMiles respeta el límite entre 3 y 4 cifras", () => {
  assert.equal(formatearMiles(999), "999");
  assert.equal(formatearMiles(1000), "1.000");
});

test("formatearMiles reagrupa mientras el usuario sigue escribiendo", () => {
  // El campo mostraba 1.500.000 y el usuario digitó otro 0 al final
  assert.equal(formatearMiles("1.500.0000"), "15.000.000");
});