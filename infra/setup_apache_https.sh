#!/usr/bin/env bash
# HU-13: Apache con HTTPS (certificado autofirmado) en WSL/Ubuntu. Ejecutar UNA vez: sudo bash infra/setup_apache_https.sh
set -euo pipefail

apt-get update
apt-get install -y apache2 openssl

# Certificado autofirmado para localhost (365 días). La llave privada queda fuera del repositorio.
mkdir -p /etc/ssl/sefi
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout /etc/ssl/sefi/sefi.key -out /etc/ssl/sefi/sefi.crt \
  -subj "/C=CO/ST=Antioquia/L=Medellin/O=SEFI-Personal/CN=localhost"
chmod 600 /etc/ssl/sefi/sefi.key

cp "$(dirname "$0")/sefi-ssl.conf" /etc/apache2/sites-available/sefi-ssl.conf
a2enmod ssl rewrite headers
a2ensite sefi-ssl
a2dissite 000-default || true
cp "$(dirname "$0")/sefi-http.conf" /etc/apache2/sites-available/sefi-http.conf
a2ensite sefi-http

# El usuario del runner debe poder escribir en el directorio público (sin usar sudo en el pipeline)
chown -R "${SUDO_USER:-$USER}":www-data /var/www/html

apache2ctl configtest
service apache2 restart
echo "Listo: https://localhost/"
