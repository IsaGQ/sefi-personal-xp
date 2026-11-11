# SEFI-Personal (kit inicial)

Punto de partida del Entregable 3 (XP: TDD, CI y CD). Aquí **todavía no están las funciones nuevas**: se construyen una por una con el ciclo Red, Green, Refactor.

| Carpeta | Contenido |
|---|---|
| `python_project/` | Motor financiero de la Etapa 1 (`financial_engine.py`) y sus pruebas con `unittest` |
| `javascript_project/` | Lógica del cliente y sus pruebas con `node --test` |
| `web/` | Página que se despliega en Apache |
| `.github/workflows/ci.yml` | Pipeline de CI/CD |

Ejecutar las pruebas (desde la raíz del repositorio):

```
python -m unittest discover -s python_project/tests -t python_project -v
cd javascript_project
npm test
```
