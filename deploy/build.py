#!/usr/bin/env python3
"""Gera site/index.html e site/jornada.html a partir das fontes em src/.

Uso: python3 deploy/build.py
- src/Landing Jornada GCC.dc.html -> site/index.html
- src/Jornada GCC.dc.html        -> site/jornada.html
Troca os links entre as páginas, aponta a imagem do topo para img/hero.jpg
e insere <title>/<meta description>.
"""
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
    assert s.count(VIEWPORT) == 1, src
    title, desc = META[dst]
    s = s.replace(VIEWPORT, VIEWPORT + f'\n<title>{title}</title>\n<meta name="description" content="{desc}">\n<meta name="robots" content="index, follow">')
    (ROOT / 'site' / dst).write_text(s, encoding='utf-8')
    print('ok', dst)
