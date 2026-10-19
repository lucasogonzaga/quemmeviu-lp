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
