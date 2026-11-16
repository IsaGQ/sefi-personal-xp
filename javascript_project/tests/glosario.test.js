const test = require("node:test");
const assert = require("node:assert/strict");
const { obtenerDefinicion } = require("../src/glosario.js");

test("obtenerDefinicion explica los términos sin importar mayúsculas ni espacios", () => {
  assert.match(obtenerDefinicion("día de quiebre"), /saldo se vuelve negativo/);
  assert.match(obtenerDefinicion("gasto hormiga"), /pequeños y frecuentes/);
  assert.match(obtenerDefinicion("TIR"), /Tasa Interna de Retorno/);
  assert.equal(obtenerDefinicion("  VAN "), obtenerDefinicion("van"));
});

test("obtenerDefinicion lanza error con términos que no están en el glosario", () => {
  assert.throws(() => obtenerDefinicion("inflación"), { message: /no está en el glosario/ });
  assert.throws(() => obtenerDefinicion("constructor"), { message: /no está en el glosario/ });
});