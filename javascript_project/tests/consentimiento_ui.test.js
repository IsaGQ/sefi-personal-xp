const test = require("node:test");
const assert = require("node:assert/strict");
const { puedeContinuar } = require("../src/consentimiento_ui.js");

test("HU-12: solo se continúa si el usuario aceptó explícitamente", () => {
  assert.equal(puedeContinuar(true), true);
  assert.equal(puedeContinuar(false), false);
  assert.equal(puedeContinuar(undefined), false);
});
