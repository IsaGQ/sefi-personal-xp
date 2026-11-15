const test = require("node:test");
const assert = require("node:assert/strict");
const { validarCorreo, validarContrasena } = require("../src/cuenta_ui.js");

test("HU-14: valida el formato del correo", () => {
  assert.equal(validarCorreo("susana@correo.com"), true);
  assert.equal(validarCorreo("susana@correo"), false);
});

test("HU-14: la contraseña necesita al menos 8 caracteres", () => {
  assert.equal(validarContrasena("12345678"), true);
  assert.equal(validarContrasena("1234567"), false);
});
