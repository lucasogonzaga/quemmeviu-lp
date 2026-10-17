# Quem Me Viu — Landing Page Jornada GCC

- `site/` — arquivos publicados (landing em `index.html`, jornada em `jornada.html`).
- `deploy/setup-server.sh` — configura nginx na VPS (Amazon Linux 2023). Idempotente.
- `.github/workflows/deploy.yml` — publica na VPS a cada push na `main` (ou manualmente em Actions → "Publicar LP na VPS" → Run workflow).

Segredos necessários (Settings → Secrets and variables → Actions):
`VPS_HOST`, `VPS_USER`, `VPS_SSH_KEY`, `VPS_PATH` e, opcional, `VPS_PORT`.
