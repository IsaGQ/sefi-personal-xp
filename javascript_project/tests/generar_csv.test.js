const test = require("node:test");
const assert = require("node:assert/strict");
const { generarCSV } = require("../src/generar_csv.js");

test("generarCSV crea el encabezado y una fila por día", () => {
  assert.equal(generarCSV([100, 50, -20]), "dia,saldo\n1,100\n2,50\n3,-20");
});

test("generarCSV rechaza listas vacías y valores que no son números", () => {
  assert.throws(() => generarCSV([]), { message: /al menos un saldo/ });
  assert.throws(() => generarCSV([100, "x"]), { message: /números/ });
});