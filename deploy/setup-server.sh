#!/usr/bin/env bash
# Configura o servidor (Amazon Linux 2023) para servir a LP com nginx.
# Idempotente: pode rodar a cada publicação sem efeito colateral.
# Uso (como root): setup-server.sh <pasta-do-site> <usuario-dono> [dominio]
# Com [dominio] (ex.: www.quemmeviu.com.br) e certificado já emitido em /etc/letsencrypt/live/<dominio>/,
# liga o HTTPS, redireciona HTTP e o domínio sem www, e ativa o HSTS. Veja docs/HTTPS.md.
set -euo pipefail
SITE_PATH="${1:?pasta do site}"
OWNER="${2:?usuario dono}"
DOMAIN="${3:-}"
APEX="${DOMAIN#www.}"
CERT="/etc/letsencrypt/live/${DOMAIN}"
HTTPS=0
[ -n "$DOMAIN" ] && [ -s "$CERT/fullchain.pem" ] && HTTPS=1
[ -n "$DOMAIN" ] && [ "$HTTPS" = 0 ] && echo "Aviso: sem certificado em $CERT; configurando só HTTP."

command -v nginx >/dev/null 2>&1 || dnf install -y nginx
command -v rsync >/dev/null 2>&1 || dnf install -y rsync

mkdir -p "$SITE_PATH"
chown -R "$OWNER":"$OWNER" "$SITE_PATH"
chmod 755 "$SITE_PATH"
if command -v chcon >/dev/null 2>&1; then chcon -R -t httpd_sys_content_t "$SITE_PATH" 2>/dev/null || true; fi

# O server padrão do nginx.conf deixa de ser o default; o da LP assume.
sed -i 's/ default_server//g' /etc/nginx/nginx.conf

# add_header em um location descarta os do server; por isso os cabeçalhos ficam num arquivo incluído nos três lugares.
cat > /etc/nginx/lp-security-headers.conf <<'HDR'
# Cabeçalhos de segurança.
add_header X-Content-Type-Options "nosniff" always;
add_header X-Frame-Options "DENY" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header Permissions-Policy "camera=(), microphone=(), geolocation=()" always;
add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://www.googletagmanager.com https://www.clarity.ms https://scripts.clarity.ms https://www.googleadservices.com https://googleads.g.doubleclick.net; style-src 'self' 'unsafe-inline'; img-src 'self' data: https://pagead2.googlesyndication.com https://*.doubleclick.net https://www.googleadservices.com https://www.googletagmanager.com https://www.google.com https://www.google.com.br https://googleads.g.doubleclick.net https://*.google-analytics.com https://*.clarity.ms https://c.bing.com; font-src 'self'; connect-src 'self' https://pagead2.googlesyndication.com https://*.doubleclick.net https://www.googletagmanager.com https://*.google-analytics.com https://*.analytics.google.com https://*.googleadservices.com https://googleads.g.doubleclick.net https://www.google.com https://www.google.com.br https://*.clarity.ms https://c.bing.com; frame-src https://www.googletagmanager.com https://td.doubleclick.net https://bid.g.doubleclick.net; frame-ancestors 'none'; base-uri 'self'; form-action 'self'" always;
HDR
if [ "$HTTPS" = 1 ]; then
  echo 'add_header Strict-Transport-Security "max-age=31536000" always;' >> /etc/nginx/lp-security-headers.conf
fi

SITE_BLOCK=$(cat <<NGINX
    root ${SITE_PATH};
    index index.html;
    charset utf-8;

    server_tokens off;

    include /etc/nginx/lp-security-headers.conf;

    gzip on;
    gzip_types text/css application/javascript image/svg+xml text/html;

    location / {
        try_files \$uri \$uri/ \$uri.html =404;
    }
    location ~* \.(png|jpe?g|svg|js|css|webp|woff2)\$ {
        expires 7d;
        add_header Cache-Control "public";
        include /etc/nginx/lp-security-headers.conf;
    }
    location ~* \.html\$ {
        add_header Cache-Control "no-cache";
        include /etc/nginx/lp-security-headers.conf;
    }
NGINX
)

if [ "$HTTPS" = 1 ]; then
cat > /etc/nginx/conf.d/quemmeviu-lp.conf <<NGINX
# Porta 80: só o desafio do Let's Encrypt (renovação) e redirecionamento para HTTPS.
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name _;
    location /.well-known/acme-challenge/ { root ${SITE_PATH}; }
    location / { return 301 https://${DOMAIN}\$request_uri; }
}
# Domínio sem www -> www
server {
    listen 443 ssl;
    listen [::]:443 ssl;
    http2 on;
    server_name ${APEX};
    ssl_certificate ${CERT}/fullchain.pem;
    ssl_certificate_key ${CERT}/privkey.pem;
    include /etc/nginx/lp-security-headers.conf;
    return 301 https://${DOMAIN}\$request_uri;
}
server {
    listen 443 ssl default_server;
    listen [::]:443 ssl default_server;
    http2 on;
    server_name ${DOMAIN};
    ssl_certificate ${CERT}/fullchain.pem;
    ssl_certificate_key ${CERT}/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
${SITE_BLOCK}
}
NGINX
else
cat > /etc/nginx/conf.d/quemmeviu-lp.conf <<NGINX
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name _;
${SITE_BLOCK}
}
NGINX
fi

nginx -t
systemctl enable --now nginx
systemctl reload nginx
echo "Servidor pronto: ${SITE_PATH}"
