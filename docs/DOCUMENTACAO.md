# Documentação — LP Jornada GCC · Quem Me Viu

Atualizado em 17/10/2026.

## 1. Visão geral

A landing page da campanha da Quem Me Viu, GCC credenciada pela SENATRAN, tem dois públicos. O principal são empresas privadas que usam dados da SENATRAN e precisam contratar uma GCC por causa da Portaria 139/2025. O outro são empresas que ainda estão no Credencia ou contratando o Serpro.

O projeto tem duas páginas:

| Página | Objetivo |
|---|---|
| **Landing** (`index.html`) | Apresentar a Quem Me Viu e levar o visitante para a Jornada interativa ou direto para o WhatsApp. |
| **Jornada GCC** (`jornada.html`) | Fazer de 1 a 5 perguntas, mostrar em que etapa a empresa está e qual é o próximo passo, e levar ao WhatsApp com uma mensagem própria para cada resultado. |

Endereço no ar: **http://44.204.204.85** (a Jornada fica em `/jornada.html`). O site ainda não tem HTTPS; veja a seção 9.

---

## 2. Onde estão os arquivos

### Pasta local: `~/Documents/ChatGPT/LP Quem me viu/`

| Item | O que é |
|---|---|
| `Landing Jornada GCC.dc.html` | Landing. Fonte editável no formato Claude Design. |
| `Jornada GCC.dc.html` | Jornada interativa. Fonte editável. |
| `support.js` | Código que faz as páginas `.dc.html` funcionarem. Carrega o React 18.3.1 do unpkg. |
| `logos/` | `logo-quem-me-viu.svg` (com o nome em verde), `logo-quem-me-viu-branco.svg`, `logo-quem-me-viu-azul.svg` e `jb3.png`. |
| `uploads/` | `hero-sp.jpg` (imagem do topo) e `comite/` (fotos dos 7 membros do comitê). |
| `dados/comite-consultivo.md` | Lista oficial do comitê, com nome, área, empresas e LinkedIn. |
| `ALTERACOES.md` | Histórico de todas as alterações, organizadas por lote. |
| `DOCUMENTACAO.md` | Este documento. |
| `docs/` | Originais: a versão do Claude Design, os logos, as fotos e as imagens. **Não alterar.** |

### Repositório GitHub: `lucasogonzaga/quemmeviu-lp` (público)

| Item | O que é |
|---|---|
| `src/` | Cópia das duas fontes `.dc.html`. É de onde o build gera o site. |
| `site/` | O que vai para o ar: `index.html`, `jornada.html`, `support.js`, `logos/`, `img/hero.jpg` e `uploads/comite/`. |
| `deploy/build.py` | Gera `site/index.html` e `site/jornada.html` a partir de `src/`. |
| `deploy/setup-server.sh` | Configura o nginx na VPS. Pode rodar quantas vezes for preciso sem efeito colateral. |
| `.github/workflows/deploy.yml` | Publica na VPS a cada atualização da branch `main`. |
| `CLAUDE.md` | Instruções resumidas para o Claude Code continuar o trabalho. |

O repositório está público porque, na conta, as automações do GitHub (Actions) só rodam em repositórios públicos; nos privados elas dependem de faturamento. Os segredos continuam protegidos.

---

## 3. Landing: seções em ordem

1. **Abertura**
   - Topo: logo da Quem Me Viu (73 px) e, à direita, "uma empresa do grupo" com o logo da JB3.
   - Selo "GCC credenciada pela SENATRAN".
   - Título: "A hora de contratar uma GCC é agora."
   - Subtítulo: "As empresas que mais usam dados da SENATRAN optaram pela Quem Me Viu. **Agora é a sua vez.**"
   - Botões: "Fazer a Jornada GCC interativa →" (verde) e "Falar com um consultor" (WhatsApp), cada um com uma linha de apoio embaixo.
2. **Clientes**
   - Três boxes com borda verde e brilho: B3, PID e Icetran.
   - Dois depoimentos:
     - Nathan Moojen, Founder, PID. A luz verde vem do canto inferior esquerdo.
     - Lisiane Fogaça Chaussard, CEO, Icetran. A luz verde vem do canto inferior direito.
3. **A Jornada GCC em 3 etapas**
   - Etapas animadas: 1. Aprovação no Credencia · 2. Contratação do Serpro e da GCC · 3. Operação.
   - Faixa verde com o logo azul: "Apoio jurídico, técnico e operacional" e "Melhor jornada assistida da aprovação no Credencia até a operação." O texto fica no azul do fundo.
   - Preço: "**O preço é o mesmo em todas as GCCs: R$ 0,80** por evento de consentimento ou ciência, definido em portaria. Sem taxa de setup e sem franquia mínima." O valor aparece em verde.
4. **Por que a Quem Me Viu?** São 6 cards, cada um com ícone e título:
   - Empresa especializada em GCC
   - Capacidade para lidar com alto volume de transações
   - Menor tempo de resposta do mercado
   - Homologação e integração assistidas
   - Atendimento humano consultivo disponível 24/7
   - Plataforma web e API de fácil utilização
5. **Comitê consultivo externo**
   - Subtítulo: "A Quem Me Viu conta com um comitê consultivo externo e crítico, formado por executivos com o mesmo perfil dos clientes que atende. São eles que desafiam e validam a nossa entrega. Nós temos o prazer de apresentar cada pessoa que faz tamanha diferença."
   - Carrossel com 7 cards. Cada card tem foto, nome, área em verde e link para o LinkedIn.
6. **Fechamento**
   - Título: "Em qualquer etapa da Jornada GCC, conte com a Quem Me Viu."
   - Os mesmos dois botões da abertura.
7. **Perguntas frequentes**, em sanfona com 4 perguntas:
   - Já contratei o Serpro. Preciso de uma GCC?
   - Posso contratar a GCC antes da aprovação?
   - Quanto custa?
   - Como funciona a integração?
8. **Rodapé**
   - À esquerda: logo da Quem Me Viu e "uma empresa do grupo" com o logo da JB3.
   - À direita: bloco Contatos, com DPO, Comercial e Suporte lado a lado, e na linha de baixo o telefone (11) 92636-3815, o LinkedIn e o Instagram.
   - Barra inferior:
     - "Quem Me Viu é uma solução da JB3 Softwares S.A. | CNPJ: 58.493.015/0001-19 | São Paulo/SP";
     - "Documento de credenciamento Senatran →", ainda sem link;
     - Copyright 2026;
     - selos ISO e SSL.

### Comitê consultivo (7 membros)

| Nome | Área | LinkedIn |
|---|---|---|
| Vitor Magnani | Finanças | linkedin.com/in/vmagnani |
| Gustavo Mistrinelli | Produto | linkedin.com/in/guga-m |
| Samanta Oliveira | Proteção de Dados | linkedin.com/in/samantaoliveiraa |
| Glaucia Miyazaki | Produto | linkedin.com/in/glaucias |
| Bruno Salles | Produto | linkedin.com/in/brunocpsalles |
| André Trench | Finanças | linkedin.com/in/andré-trench-4a369894 |
| Patricia Cardoso | Tecnologia e Produto | linkedin.com/in/patricia-cardoso-7a166920 |

---

## 4. Jornada GCC: lógica

No topo da página aparecem:
- o trilho das 3 etapas, com um marcador da posição atual nas perguntas e o selo "Você está aqui" no resultado;
- a faixa "Apoio jurídico, técnico e operacional da Quem Me Viu".

### Perguntas

| # | Pergunta | Respostas → destino |
|---|---|---|
| P1 | Sua empresa já fez a solicitação no Credencia? | Ainda não → R1 · Comecei, mas está em rascunho → R1 · Sim, já enviei → P2 |
| P2 | Qual é a situação dos seus casos de uso? | Em análise pela SENATRAN → R2 · Devolvido para ajustes → R3 · Não aprovado → R4 · Aprovado em parte → R5 · **Aprovado** (em destaque) → P3 |
| P3 | Sua empresa já contratou o serviço de dados do Serpro (Consulta Online ou Datavalid)? | Ainda não → R6 · Sim → P4 |
| P4 | Sua empresa já contratou uma GCC? | **Ainda não** (em destaque) → R7 · Sim → P5 |
| P5 | Sua operação já está em produção? | Ainda não → R8 · Sim → R9 |

### Resultados e mensagens do WhatsApp

Todas as mensagens seguem a estrutura **[contexto] + [solução Quem Me Viu]**. Como cada uma começa diferente, dá para saber de onde veio o contato.

| Resultado | Etapa | Mensagem |
|---|---|---|
| R1 · Hora de começar pelo Credencia | 1 | Olá! Ainda não enviei os casos de uso ao Credencia. Quero o apoio da Quem Me Viu para estruturar o pedido. |
| R2 · Seu pedido está em análise | 1 | Olá! Meu pedido no Credencia está em análise. Quero já contratar e homologar a GCC com a Quem Me Viu. |
| R3 · Seu pedido voltou para ajustes | 1 | Olá! Meu pedido no Credencia voltou para ajustes. Quero o apoio da Quem Me Viu para corrigir e reenviar. |
| R4 · Seu pedido não foi aprovado | 1 | Olá! Meu pedido no Credencia não foi aprovado. Quero o apoio da Quem Me Viu para refazer o pedido. |
| R5 · Seu pedido foi aprovado em parte | 1 e 2 | Olá! Meu pedido no Credencia foi aprovado em parte. Quero o apoio da Quem Me Viu para avançar nas duas frentes. |
| R6 · Aprovado! Agora é contratar | 2 | Olá! Meu pedido no Credencia foi aprovado. Quero contratar o Serpro e a Quem Me Viu como minha GCC. |
| R7 · Falta só a GCC | 2 | Olá! Já tenho o Serpro e falta a GCC. Quero contratar a Quem Me Viu. |
| R8 · Rumo à produção | 3 | Olá! Estou na fase de integração e homologação com o Serpro. Quero o apoio da Quem Me Viu para entrar em produção. |
| R9 · Operação em andamento | 3 | Olá! Minha empresa já opera no novo modelo. Quero conhecer o suporte da Quem Me Viu e falar sobre novos casos de uso. |

### Mensagens da landing

| Botão | Mensagem |
|---|---|
| Topo | Olá! Minha empresa precisa contratar uma GCC. Quero conhecer a solução da Quem Me Viu. |
| Fechamento | Olá! Conheci a Jornada GCC. Quero que a Quem Me Viu acompanhe minha empresa em todas as etapas. |
| Telefone do rodapé | Olá! Tenho dúvidas sobre a GCC. Quero falar com a Quem Me Viu. |

O número de todas as mensagens é o WhatsApp +55 11 92636-3815. O contato pode editar o texto antes de enviar, então a contagem por origem é uma boa aproximação, mas não é exata.

### Botões de navegação

- **"← Voltar":** verde e com brilho, sempre à esquerda. Na primeira pergunta ele leva à página inicial.
- **À direita:** "Voltar para a página inicial" e, no resultado, também "Refazer a jornada". Os dois no estilo branco.
- **Tela de resultado:** tem uma coluna só. O box "Seu próximo passo" traz o botão do WhatsApp e a frase "Uma pessoa de verdade, não um robô."

---

## 5. Identidade visual

| Uso | Cor |
|---|---|
| Fundo (azul-marinho) | `#0d1d4f` |
| Superfícies e cards | `#10215a` → `#172a66` (degradê) |
| Verde da marca (botões, destaques, brilhos) | `#4ff59a` (hover `#9dffc6`) |
| Texto principal | `#eef3f7` |
| Texto secundário | `#b9c6d2` / `#dce5ec` |
| Texto sobre o verde | `#0d1d4f` (botões verdes: `#06120b`) |
| Rodapé | `#0b1945` |

- **Fontes:** Sora para títulos e DM Sans para textos, as duas do Google Fonts.
- **Brilho (glow):** é usado nos boxes de clientes, nos cards de resposta em destaque ("Aprovado" e "Ainda não", este na pergunta sobre a GCC) e no botão "Voltar".

---

## 6. Como fazer uma alteração

1. Editar a fonte `.dc.html` na pasta local, ou em `src/` no repositório.
2. Abrir a página no navegador e conferir no computador e no celular.
3. Copiar as fontes para `src/` no repositório, se a edição foi feita na pasta local, e rodar `python3 deploy/build.py`.
4. Enviar a alteração para a branch `main`. A automação publica sozinha em menos de um minuto.
5. Registrar a alteração no `ALTERACOES.md`.

A imagem do topo vira `img/hero.jpg` no site: na pasta local ela é `uploads/hero-sp.jpg`, e o build ajusta o caminho. Para trocar a imagem, recorte a nova na proporção de cerca de 1,83:1 e substitua os dois arquivos.

Combinado de trabalho com o Lucas:
- As alterações chegam uma a uma. Anote todas e execute só quando ele pedir.
- Ao executar, salve na pasta local e publique online.
- Avise quando publicar. Não precisa mandar imagens nem conferir no GitHub.

---

## 7. Publicação (deploy)

O arquivo `.github/workflows/deploy.yml` roda a cada envio para a `main` e faz cinco coisas:

1. Confere se os segredos existem.
2. Prepara a chave SSH, que fica guardada como segredo no GitHub e nunca aparece.
3. Roda `deploy/setup-server.sh` na VPS: instala o nginx e o rsync se faltarem, cria `/var/www/lp` e configura o nginx.
4. Envia o conteúdo de `site/` com rsync, apagando no servidor o que não existe mais.
5. Confere se `http://<IP>/` responde 200.

Para publicar manualmente, vá em GitHub → Actions → "Publicar LP na VPS" → Run workflow.

### Segredos do repositório (Settings → Secrets and variables → Actions)

| Segredo | Valor |
|---|---|
| `VPS_HOST` | 44.204.204.85 |
| `VPS_USER` | ec2-user |
| `VPS_PATH` | /var/www/lp |
| `VPS_SSH_KEY` | Conteúdo da chave `website_jb3.pem`, cadastrado pelo Lucas |
| `VPS_PORT` | Não usado (padrão 22) |

---

## 8. Servidor

- **Hospedagem:** AWS Lightsail, Amazon Linux 2023, região us-east-1a.
- **Acesso:** usuário `ec2-user`, chave "website".
- **Servidor web:** nginx, configurado em `/etc/nginx/conf.d/quemmeviu-lp.conf`. Faz cache de 7 dias para imagens e scripts; os HTML não ficam em cache.
- **IP público:** 44.204.204.85. **Ainda não é estático**, então muda se a instância for reiniciada.
- **Firewall do Lightsail:** as portas 22 e 80 estão abertas. A 443 (HTTPS) precisa ser liberada.
- O Lucas não tem acesso ao painel da AWS. Mudanças de firewall e de IP dependem de quem administra a conta.

---

## 9. Pendências

| Item | O que falta | Quem resolve |
|---|---|---|
| **HTTPS / domínio** | Definir o subdomínio da campanha (ex.: lp.quemmeviu.com.br) e onde está o DNS. Se for Cloudflare: registro com proxy e SSL "Flexible". Se for outro: registro A para o IP, liberar a porta 443 e emitir o certificado pela automação. | Lucas / admin da AWS e do DNS |
| **IP estático** | Criar um static IP no Lightsail e atualizar o `VPS_HOST`, se o IP mudar. | Admin da AWS |
| **Credenciamento Senatran** | Link ou PDF para o "Documento de credenciamento Senatran →" do rodapé. | Lucas / cliente |
| **Validações do cliente** | Autorização para citar a B3, papel da Baptista Luz, escopo do atendimento 24/7. | Cliente |
| **Selos ISO** | Os selos ISO (27001 · 27701 · 27018 · 9001) saíram dos cards. Foi proposta uma linha de selos, ainda não aprovada. | Lucas |
| **Logo branco** | Decidir se o logo branco também entra no topo e no rodapé. Hoje está o logo verde. | Lucas |

---

## 10. Histórico

O registro detalhado de cada alteração, lote a lote, está no `ALTERACOES.md`, nesta mesma pasta.
