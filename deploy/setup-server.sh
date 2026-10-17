#!/usr/bin/env bash
# Configura o servidor (Amazon Linux 2023) para servir a LP com nginx.
# Idempotente: pode rodar a cada publicação sem efeito colateral.
# Uso (como root): setup-server.sh <pasta-do-site> <usuario-dono>
set -euo pipefail
SITE_PATH="${1:?pasta do site}"
OWNER="${2:?usuario dono}"

command -v nginx >/dev/null 2>&1 || dnf install -y nginx
command -v rsync >/dev/null 2>&1 || dnf install -y rsync

mkdir -p "$SITE_PATH"
chown -R "$OWNER":"$OWNER" "$SITE_PATH"
chmod 755 "$SITE_PATH"
if command -v chcon >/dev/null 2>&1; then chcon -R -t httpd_sys_content_t "$SITE_PATH" 2>/dev/null || true; fi

# O server padrão do nginx.conf deixa de ser o default; o da LP assume.
sed -i 's/ default_server//g' /etc/nginx/nginx.conf

cat > /etc/nginx/conf.d/quemmeviu-lp.conf <<NGINX
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name _;
    root ${SITE_PATH};
    index index.html;
    charset utf-8;

    gzip on;
    gzip_types text/css application/javascript image/svg+xml text/html;

    location / {
        try_files \$uri \$uri/ \$uri.html =404;
    }
    location ~* \.(png|jpe?g|svg|js|css|webp)$ {
        expires 7d;
        add_header Cache-Control "public";
    }
    location ~* \.html$ {
        add_header Cache-Control "no-cache";
    }
}
NGINX

nginx -t
systemctl enable --now nginx
systemctl reload nginx
echo "Servidor pronto: ${SITE_PATH}"
