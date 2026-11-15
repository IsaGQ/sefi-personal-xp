# HU-13: despliegue con HTTPS y runner self-hosted

## 1. Apache con HTTPS (WSL)

    sudo bash infra/setup_apache_https.sh
    curl -k https://localhost/

La página debe responder con el contenido de SEFI-Personal. En el navegador aparece el candado; al ser un certificado autofirmado, el navegador pide aceptarlo una vez (es lo esperado en un ambiente de pruebas).

## 2. Runner self-hosted (en WSL)

En GitHub: Settings, Actions, Runners, New self-hosted runner, Linux x64. Copia los comandos que muestra la página. El token NO se sube al repositorio.

    mkdir actions-runner && cd actions-runner
    ./config.sh --url https://github.com/<usuario>/<repo> --token <TOKEN_DE_GITHUB>
    ./run.sh

Deja ./run.sh corriendo mientras haces push a main: el job deploy usa runs-on: [self-hosted, linux].

## 3. Plan B si falla el hosting (CA3 de HU-13)

Con las pruebas pasando en local, ejecutar bash infra/setup_apache_https.sh y copiar web/ y javascript_project/src/*.js a /var/www/html/ levanta el portal en menos de 15 minutos.
