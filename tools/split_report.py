"""Divide el informe (README.md) en un archivo por capitulo para que GitHub lo muestre completo.

GitHub deja de renderizar un Markdown cuando el resultado supera cierto tamaño. El informe se
reparte en README.md (secciones iniciales e indice), capitulo-1.md ... capitulo-6.md y cierre.md.
Los enlaces internos se reapuntan al archivo donde quedo su destino. El contenido no cambia.

Uso: python tools/split_report.py            (lee README.md y escribe los archivos)
     python tools/join_report.py > informe.md (vuelve a unirlos para exportar a PDF)
"""
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PARTS = [  # (archivo, titulo de primer nivel con el que empieza, etiqueta para la navegacion)
    ('README.md', None, 'Inicio'),
    ('capitulo-1.md', 'Capítulo I:', 'Capítulo I'),
    ('capitulo-2.md', 'Capítulo II:', 'Capítulo II'),
    ('capitulo-3.md', 'Capítulo III:', 'Capítulo III'),
    ('capitulo-4.md', 'Capítulo IV:', 'Capítulo IV'),
    ('capitulo-5.md', 'Capítulo V:', 'Capítulo V'),
    ('capitulo-6.md', 'Capítulo VI:', 'Capítulo VI'),
    ('cierre.md', 'Conclusiones', 'Conclusiones, Bibliografía y Anexos'),
]
NAV_START, NAV_END = '<!-- nav:start -->', '<!-- nav:end -->'


def heading_text(line):
    t = re.sub(r'^#{1,6}\s+', '', line).strip()
    t = re.sub(r'<[^>]+>', '', t)
    t = re.sub(r'!?\[([^\]]*)\]\([^)]*\)', r'\1', t)
    t = re.sub(r'(\*\*|__|\*|`)', '', t)
    t = re.sub(r'(?<![\w])_|_(?![\w])', '', t)
    return t.strip()


def slug(text):
    t = text.lower()
    t = ''.join(c for c in t if c.isalnum() or c in ' -_' or unicodedata.category(c).startswith('M'))
    return t.replace(' ', '-')


def anchors(lines):
    """Devuelve [(indice_de_linea, ancla)] con los ids explicitos y los slugs de GitHub (con sufijos)."""
    seen, out, fence = {}, [], False
    for i, line in enumerate(lines):
        if line.lstrip().startswith('```'):
            fence = not fence
            continue
        if fence:
            continue
        for m in re.finditer(r'\b(?:id|name)="([^"]+)"', line):
            out.append((i, m.group(1)))
        if re.match(r'^#{1,6}\s', line):
            base = slug(heading_text(line))
            n = seen.get(base, 0)
            seen[base] = n + 1
            out.append((i, base if n == 0 else f'{base}-{n}'))
    return out


def split(text):
    lines = text.split('\n')
    starts = [0]
    for _, title, _ in PARTS[1:]:
        idx = next(i for i, l in enumerate(lines) if re.match(r'^#\s+\**\s*' + re.escape(title), l))
        while idx > 0 and re.match(r'^\s*<a (id|name)="[^"]*"></a>\s*$', lines[idx - 1]):
            idx -= 1  # el ancla explicita viaja con su titulo
        starts.append(idx)
    bounds = list(zip(starts, starts[1:] + [len(lines)]))
    owner = {}
    for (f, _, _), (a, b) in zip(PARTS, bounds):
        for i in range(a, b):
            owner[i] = f
    # ancla original -> (archivo, ancla en ese archivo)
    old = anchors(lines)
    pieces = {f: lines[a:b] for (f, _, _), (a, b) in zip(PARTS, bounds)}
    new_by_line = {}
    for (f, _, _), (a, _) in zip(PARTS, bounds):
        for j, anc in anchors(pieces[f]):
            new_by_line.setdefault(a + j, []).append(anc)
    target = {}
    for i, anc in old:
        cands = new_by_line.get(i, [])
        new = anc if anc in cands else next((c for c in cands if c.rsplit('-', 1)[0] == anc.rsplit('-', 1)[0]), anc)
        target.setdefault(anc, (owner[i], new))

    def fix(line, here):
        def rep(m, pre, post):
            anc = m.group(2)
            if anc not in target:
                return m.group(0)
            f, new = target[anc]
            return f'{m.group(1)}{"" if f == here else f}#{new}{post}'
        line = re.sub(r'(href=")#([^"]+)(")', lambda m: rep(m, 'href="', '"'), line)
        line = re.sub(r'(\]\()#([^)\s]+)(\))', lambda m: rep(m, '](', ')'), line)
        return line

    out = {}
    for k, (f, _, label) in enumerate(PARTS):
        body = [fix(l, f) for l in pieces[f]]
        prev = PARTS[k - 1] if k > 0 else None
        nxt = PARTS[k + 1] if k + 1 < len(PARTS) else None
        links = []
        if prev:
            links.append(f'<a href="{prev[0]}">← {prev[2]}</a>')
        if k > 0:
            links.append(f'<a href="README.md#contenido">Contenido</a>')
        if nxt:
            links.append(f'<a href="{nxt[0]}">{nxt[2]} →</a>')
        nav = f'{NAV_START}\n<p align="center">{" · ".join(links)}</p>\n{NAV_END}'
        if k == 0:
            out[f] = '\n'.join(body).rstrip('\n') + '\n\n' + nav + '\n'
        else:
            out[f] = nav + '\n\n' + '\n'.join(body).rstrip('\n') + '\n\n' + nav + '\n'
    return out, target


def main():
    text = (ROOT / 'README.md').read_text(encoding='utf-8')
    if NAV_START in text:
        raise SystemExit('README.md ya esta dividido: une primero con join_report.py')
    out, _ = split(text)
    for f, content in out.items():
        (ROOT / f).write_text(content, encoding='utf-8', newline='\n')
        print(f'{f}: {len(content.encode("utf-8")) // 1024} KB')


if __name__ == '__main__':
    main()
