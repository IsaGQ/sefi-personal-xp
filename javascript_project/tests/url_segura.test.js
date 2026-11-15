const test = require("node:test");
const assert = require("node:assert/strict");
const { esUrlSegura } = require("../src/url_segura.js");

test("HU-13: solo las URL https se consideran seguras", () => {
  assert.equal(esUrlSegura("https://localhost/"), true);
  assert.equal(esUrlSegura("http://localhost/"), false);
  assert.equal(esUrlSegura("no es una url"), false);
});
