#!/usr/bin/env python3
"""Gera site/index.html e site/jornada.html a partir das fontes em src/.

Uso: python3 deploy/build.py
- src/legal/*.html (texto) -> site/politica-de-privacidade.html e site/termos-de-uso.html
- src/Landing Jornada GCC.dc.html -> site/index.html
- src/Jornada GCC.dc.html        -> site/jornada.html
Troca os links entre as páginas, troca o Google Fonts pelas fontes locais (fonts/fonts.css), aponta a imagem do topo para img/hero.jpg
e insere <title>/<meta description>.
"""
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
VIEWPORT = '<meta name="viewport" content="width=device-width, initial-scale=1">'
META = {
    'index.html': ('Quem Me Viu | GCC credenciada pela SENATRAN',
                   'A Quem Me Viu acompanha sua empresa na Jornada GCC, da aprovação no Credencia até a operação.'),
    'jornada.html': ('Jornada GCC | Quem Me Viu',
                     'Responda algumas perguntas e descubra o próximo passo da sua empresa na Jornada GCC.'),
}
for src, dst in [('Landing Jornada GCC.dc.html', 'index.html'), ('Jornada GCC.dc.html', 'jornada.html')]:
    s = (ROOT / 'src' / src).read_text(encoding='utf-8')
    s = s.replace('Landing Jornada GCC.dc.html', './').replace('Jornada GCC.dc.html', 'jornada.html')
    s = s.replace('uploads/hero-sp.jpg', 'img/hero.jpg')
    GF = re.compile(r'<link rel="preconnect" href="https://fonts\.googleapis\.com">\s*<link href="https://fonts\.googleapis\.com/css2[^"]*" rel="stylesheet">')
    assert len(GF.findall(s)) == 1, src
    s = GF.sub('<link rel="preload" href="fonts/151a53ae17.woff2" as="font" type="font/woff2" crossorigin>\n<link rel="stylesheet" href="fonts/fonts.css">', s)
    assert s.count(VIEWPORT) == 1, src
    title, desc = META[dst]
    s = s.replace(VIEWPORT, VIEWPORT + f'\n<title>{title}</title>\n<meta name="description" content="{desc}">\n<meta name="robots" content="index, follow">')
    assert '</body>' in s, src
    s = s.replace('</body>', '<script src="consent.js" defer></script>\n</body>', 1)
    (ROOT / 'site' / dst).write_text(s, encoding='utf-8')
    print('ok', dst)

LEGAL = {
    'politica-de-privacidade': 'Política de Privacidade',
    'termos-de-uso': 'Termos de Uso',
    'politica-de-seguranca': 'Política de Segurança da Informação',
    'politica-para-fornecedores': 'Política para Fornecedores',
    'politica-integrada': 'Política Integrada',
}
# Documentos da JB3 (texto copiado de jb3ti.com.br): recebem a nota de origem.
JB3_DOCS = {'politica-de-seguranca', 'politica-para-fornecedores', 'politica-integrada'}
NAV = ''.join(f'<a href="{slug}.html">{title}</a>' for slug, title in LEGAL.items())
TEMPLATE = '''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Quem Me Viu</title>
<meta name="description" content="{title} da Quem Me Viu.">
<meta name="robots" content="index, follow">
<link rel="preload" href="fonts/151a53ae17.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="fonts/fonts.css">
<style>
*{{box-sizing:border-box}}
body{{margin:0;background:#0d1d4f;color:#eef3f7;font-family:"DM Sans",system-ui,sans-serif;line-height:1.7;font-size:17px}}
header{{padding:24px clamp(20px,5vw,72px);display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap;border-bottom:1px solid rgba(255,255,255,.1)}}
header img{{height:44px;width:auto;display:block}}
a{{color:#4ff59a}}
.back{{font-size:15px;font-weight:600;text-decoration:none;border:1.5px solid #4ff59a;border-radius:999px;padding:10px 18px}}
main{{max-width:860px;margin:0 auto;padding:clamp(40px,6vw,80px) clamp(20px,5vw,40px)}}
h1{{font-family:Sora,sans-serif;font-weight:800;font-size:clamp(32px,4.4vw,52px);line-height:1.08;letter-spacing:-.025em;margin:0 0 32px}}
h2{{font-family:Sora,sans-serif;font-weight:700;font-size:clamp(22px,2.4vw,28px);margin:44px 0 12px;color:#fff}}
h3{{font-family:Sora,sans-serif;font-weight:600;font-size:19px;margin:28px 0 8px}}
p,li{{color:#dce5ec}}
li{{margin:4px 0}}
strong{{color:#fff}}
nav.docs{{padding:28px clamp(20px,5vw,72px) 8px;border-top:1px solid rgba(255,255,255,.1);display:flex;flex-wrap:wrap;gap:10px 26px;font-size:15px}}
nav.docs b{{width:100%;color:#fff;font-family:Sora,sans-serif;font-size:16px}}
.nota{{margin:-12px 0 28px;color:#b9c6d2;font-size:16px}}
footer{{padding:32px clamp(20px,5vw,72px);border-top:1px solid rgba(255,255,255,.1);font-size:14px;color:#b9c6d2;display:flex;flex-wrap:wrap;gap:12px 28px}}
</style>
</head>
<body>
<header><a href="./" aria-label="Quem Me Viu"><img src="logos/logo-quem-me-viu.svg" alt="Quem Me Viu"></a><a class="back" href="./">← Voltar para a página inicial</a></header>
<main>
<h1>{title}</h1>
{nota}{body}
</main>
<nav class="docs" aria-label="Outras políticas"><b>Políticas e documentos</b>{nav}<a href="#cookies">Definições de cookies</a></nav>
<footer><span>Quem Me Viu é uma solução da JB3 Softwares S.A. | CNPJ: 58.493.015/0001-19 | São Paulo/SP</span><a href="#cookies">Definições de cookies</a></footer>
<script src="consent.js" defer></script>
</body>
</html>
'''
for slug, title in LEGAL.items():
    body = (ROOT / 'src' / 'legal' / f'{slug}.html').read_text(encoding='utf-8')
    nota = '<p class="nota">Documento da JB3 Softwares S.A., empresa responsável pela Quem Me Viu.</p>\n' if slug in JB3_DOCS else ''
    (ROOT / 'site' / f'{slug}.html').write_text(TEMPLATE.format(title=title, body=body, nota=nota, nav=NAV), encoding='utf-8')
    print('ok', slug + '.html')

# ---------------------------------------------------------------------------
# Blog: src/blog/posts.json (lista) + src/blog/<slug>.html (texto do artigo)
#       -> site/blog/<slug>.html (página clara) e site/blog/posts.json (lido pela home)
# Para publicar um artigo novo: 1) imagem em site/blog/img/, 2) texto em src/blog/<slug>.html,
# 3) uma entrada em src/blog/posts.json, 4) python3 deploy/build.py
# ---------------------------------------------------------------------------
import json
MESES = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
SITE = 'https://www.quemmeviu.com.br'
WA_ICON = '<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3Z"/></svg>'
BLOG_TEMPLATE = '''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%%TITULO%% | Quem Me Viu</title>
<meta name="description" content="%%RESUMO%%">
<link rel="canonical" href="%%URL%%">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Quem Me Viu">
<meta property="og:title" content="%%TITULO%%">
<meta property="og:description" content="%%RESUMO%%">
<meta property="og:url" content="%%URL%%">
<meta property="og:image" content="%%IMG_ABS%%">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="/fonts/151a53ae17.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/fonts/fonts.css">
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{background:#f4f6fa;color:#1f2a44;font-family:"DM Sans",system-ui,sans-serif;line-height:1.7;-webkit-font-smoothing:antialiased}
a{color:#0d1d4f}
header{background:#fff;border-bottom:1px solid #e3e8f1}
header div{max-width:1040px;margin:0 auto;padding:18px 24px;display:flex;align-items:center;justify-content:space-between;gap:16px}
header img{height:38px;width:auto;display:block}
.voltar{font-size:15px;font-weight:600;text-decoration:none;color:#0d1d4f;border:1.5px solid #0d1d4f;border-radius:999px;padding:9px 18px}
.voltar:hover{background:#0d1d4f;color:#fff}
main{max-width:780px;margin:0 auto;padding:clamp(36px,6vw,72px) 24px 24px}
.data{font-size:15px;font-weight:600;color:#5a6785;letter-spacing:.02em}
h1{margin:12px 0 18px;font-family:Sora,sans-serif;font-weight:800;font-size:clamp(30px,4.6vw,46px);line-height:1.1;letter-spacing:-.03em;color:#0d1d4f;text-wrap:balance}
.resumo{font-size:clamp(18px,2vw,21px);line-height:1.55;color:#43506b;text-wrap:pretty}
.capa{display:block;width:100%;height:auto;margin:34px 0 40px;border-radius:20px;box-shadow:0 18px 50px -20px rgba(13,29,79,.45)}
article p{font-size:18px;line-height:1.8;margin:0 0 24px;color:#1f2a44;text-wrap:pretty}
.cta{margin:48px 0 0;padding:32px;border-radius:24px;background:#0d1d4f;color:#eef3f7;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:20px 28px}
.cta strong{display:block;font-family:Sora,sans-serif;font-size:22px;line-height:1.25;margin-bottom:4px}
.cta span{color:#b9c6d2;font-size:16px}
.btn{display:inline-flex;align-items:center;gap:10px;padding:16px 26px;border-radius:999px;background:#4ff59a;color:#06120b;font-weight:700;font-size:16px;text-decoration:none}
.btn:hover{background:#9dffc6}
footer{max-width:1040px;margin:56px auto 0;padding:28px 24px 48px;border-top:1px solid #e3e8f1;font-size:13.5px;line-height:1.7;color:#5a6785;display:flex;flex-wrap:wrap;gap:8px 28px;justify-content:space-between}
footer a{color:#43506b}
@media (max-width:520px){.cta{padding:24px}}
</style>
</head>
<body>
<header><div><a href="/" aria-label="Quem Me Viu"><img src="/logos/logo-quem-me-viu-azul.svg" alt="Quem Me Viu"></a><a class="voltar" href="/">← Voltar ao site</a></div></header>
<main>
<p class="data">%%DATA%%</p>
<h1>%%TITULO%%</h1>
<p class="resumo">%%RESUMO%%</p>
<img class="capa" src="/%%IMG%%" width="1200" height="627" alt="%%TITULO%%">
<article>
%%CORPO%%
</article>
<div class="cta"><div><strong>Já contratou a GCC para o seu negócio?</strong><span>Fale com um consultor da Quem Me Viu.</span></div>
<a class="btn" href="https://wa.me/5511926363815?text=%%WA%%" target="_blank" rel="noopener">%%WA_ICON%%Falar com um consultor</a></div>
</main>
<footer>
<span>Quem Me Viu é uma solução da <strong>JB3 Softwares S.A.</strong> | CNPJ: 58.493.015/0001-19 | São Paulo/SP</span>
<span><a href="/politica-de-privacidade.html">Política de Privacidade</a> · <a href="/termos-de-uso.html">Termos de Uso</a> · <a href="#cookies">Definições de cookies</a></span>
</footer>
<script src="/consent.js" defer></script>
</body>
</html>
'''
import html as _html, urllib.parse as _up
posts = json.loads((ROOT / 'src' / 'blog' / 'posts.json').read_text(encoding='utf-8'))
posts.sort(key=lambda p: p['data'], reverse=True)
(ROOT / 'site' / 'blog').mkdir(parents=True, exist_ok=True)
(ROOT / 'site' / 'blog' / 'posts.json').write_text(json.dumps(posts, ensure_ascii=False, indent=1), encoding='utf-8')
for p in posts:
    ano, mes, dia = map(int, p['data'].split('-'))
    wa = _up.quote(f'Olá! Li o artigo "{p["titulo"]}" e quero conversar com a Quem Me Viu.', safe='')
    corpo = (ROOT / 'src' / 'blog' / f'{p["slug"]}.html').read_text(encoding='utf-8').strip()
    out = (BLOG_TEMPLATE.replace('%%TITULO%%', _html.escape(p['titulo'])).replace('%%RESUMO%%', _html.escape(p['resumo']))
           .replace('%%URL%%', f'{SITE}/blog/{p["slug"]}.html').replace('%%IMG_ABS%%', f'{SITE}/{p["imagem"]}').replace('%%IMG%%', p['imagem'])
           .replace('%%DATA%%', f'{dia} de {MESES[mes-1]} de {ano}').replace('%%CORPO%%', corpo).replace('%%WA%%', wa).replace('%%WA_ICON%%', WA_ICON))
    (ROOT / 'site' / 'blog' / f'{p["slug"]}.html').write_text(out, encoding='utf-8')
    print('ok blog/' + p['slug'] + '.html')
