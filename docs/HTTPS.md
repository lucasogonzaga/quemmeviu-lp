# Colocar a LP em www.quemmeviu.com.br com HTTPS

Substitui o site atual. O DNS está no Route 53 (AWS). **Não alterar** os registros MX (e-mail Outlook), TXT de e-mail/verificação e NS.

Valores atuais, para reverter se preciso:
- `www.quemmeviu.com.br` → CNAME `quemmeviu.com.br`
- `quemmeviu.com.br` → A `185.158.133.1`

## 0. Antes (AWS Lightsail / Route 53) — administrador
1. Criar um **IP estático** e anexar à instância. Informar o IP ao Lucas (ele atualiza o segredo `VPS_HOST`).
2. Liberar a porta **443** (TCP) no firewall do Lightsail.
3. Um dia antes: baixar o TTL de `www` e do apex para 60 segundos.

## 1. Certificado (sem tirar nada do ar) — administrador, no servidor
```bash
sudo dnf install -y certbot
sudo certbot certonly --manual --preferred-challenges dns \
  --cert-name www.quemmeviu.com.br \
  -d www.quemmeviu.com.br -d quemmeviu.com.br
```
O certbot pede dois registros **TXT** no Route 53 (`_acme-challenge.www` e `_acme-challenge`). Criar, esperar ~1 minuto, confirmar. Remover os TXT depois.

## 2. Ligar o HTTPS no nginx — administrador, no servidor
Com o arquivo `deploy/setup-server.sh` do repositório:
```bash
sudo bash setup-server.sh /var/www/lp ec2-user www.quemmeviu.com.br
```
Testar antes da troca de DNS (de qualquer computador):
```bash
curl -sI --resolve www.quemmeviu.com.br:443:<IP_ESTATICO> https://www.quemmeviu.com.br/ | head -5
```
Esperado: `HTTP/2 200` e `strict-transport-security`.

## 3. A troca (Route 53) — administrador
1. Em `www`: remover o CNAME e criar **A** → IP estático.
2. No apex (`quemmeviu.com.br`): trocar o A `185.158.133.1` por A → IP estático.
Conferir `https://www.quemmeviu.com.br`, `https://www.quemmeviu.com.br/jornada.html` e que `http://quemmeviu.com.br` redireciona para o `www`.

## 4. Renovação automática — administrador, no servidor, depois da troca
O certificado foi emitido por DNS manual (não renova sozinho). Trocar para o método por arquivo:
```bash
sudo certbot certonly --webroot -w /var/www/lp \
  --cert-name www.quemmeviu.com.br \
  -d www.quemmeviu.com.br -d quemmeviu.com.br \
  --force-renewal --deploy-hook "systemctl reload nginx"
sudo systemctl enable --now certbot-renew.timer
sudo certbot renew --dry-run
```
Depois subir o TTL de volta ao normal.

## Reverter
Voltar os dois registros para os valores atuais acima. Com TTL de 60 s, volta em minutos.
