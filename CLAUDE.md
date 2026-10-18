# Quem Me Viu — LP Jornada GCC

Landing page da campanha da Quem Me Viu (GCC credenciada pela SENATRAN) + página interativa "Jornada GCC". Cliente da agência do Lucas. Idioma de trabalho: português.

Documentação completa: `docs/DOCUMENTACAO.md`.

## Estrutura
- `src/` — **fontes editáveis** (formato Claude Design `.dc.html`: `<x-dc>`, `<helmet>`, estilos inline, `style-hover`, `{{ }}` e um `<script type="text/x-dc">` com a lógica). Edite aqui.
  - `Landing Jornada GCC.dc.html` → landing
  - `Jornada GCC.dc.html` → jornada interativa (perguntas Q / resultados R no script)
- `site/` — o que vai para o ar. **Não editar à mão** `index.html`/`jornada.html`: rode `python3 deploy/build.py`.
  - `support.js` (runtime do Claude Design; React 18.3.1 hospedado em `vendor/`, com SRI mantido), `fonts/` (Sora e DM Sans locais, sem Google Fonts), `logos/`, `img/hero.jpg`, `uploads/comite/` (fotos do comitê).
- `deploy/setup-server.sh` — configura nginx na VPS (idempotente).
- `.github/workflows/deploy.yml` — a cada push na `main`: configura nginx, faz rsync de `site/` e checa HTTP 200.

## Fluxo de trabalho combinado com o Lucas
- Ele manda as alterações uma a uma; **anote e só execute quando ele disser** ("pode implementar"/"pode executar").
- Ao executar: editar `src/`, rodar o build, conferir visualmente, commit e push (publica sozinho). Avisar quando publicar; não precisa mandar prints nem abrir o GitHub para checar.
- Também existe a pasta local dele `~/Documents/ChatGPT/LP Quem me viu/` (mesmas fontes na raiz, `ALTERACOES.md` com o histórico, `docs/` = originais, não mexer). Mantenha-a em sincronia com `src/` se tiver acesso.

## Servidor
- AWS Lightsail, Amazon Linux 2023, usuário `ec2-user`, IP **44.204.204.85** (ainda não é IP estático).
- Site em `/var/www/lp`, nginx. Hoje só HTTP (porta 443 fechada no firewall do Lightsail; o Lucas não tem acesso à AWS).
- Segredos do Actions: `VPS_HOST`, `VPS_USER`, `VPS_DEPLOY_KEY`, `VPS_PATH` (+ `VPS_PORT` opcional). `VPS_DEPLOY_KEY` é uma chave exclusiva, restrita no servidor (`/usr/local/bin/lp-rsync-only`) a rsync em `/var/www/lp`; não dá shell. Mudanças no nginx (`deploy/setup-server.sh`) o deploy não faz mais: quem administra o servidor roda o script. Nunca peça/manuseie a chave.
- Repositório público por causa do faturamento do GitHub Actions (privado não roda).

## Pendências
- HTTPS: definir subdomínio (ex.: lp.quemmeviu.com.br) e onde está o DNS. Se Cloudflare: proxy + SSL Flexible. Senão: registro A + abrir 443 no Lightsail + certbot via workflow.
- IP estático no Lightsail.
- Link do "Documento de credenciamento Senatran" no rodapé (hoje só texto).
- Validar com o cliente: autorização para citar a B3, papel da Baptista Luz, escopo do 24/7.

## Segurança
- Cabeçalhos (CSP, nosniff, X-Frame-Options etc.) em `deploy/setup-server.sh`. Sem recursos externos: não adicione scripts/fontes/imagens de terceiros sem ajustar a CSP.
- Ativar HSTS (linha comentada no script) só depois que o HTTPS estiver no ar.
