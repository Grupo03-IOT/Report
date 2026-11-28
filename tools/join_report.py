"""Une README.md y los capitulos en un solo Markdown, en orden, para exportar el informe a PDF/Word.

Quita la navegacion entre archivos y devuelve los enlaces a anclas locales (#...).
Uso: python tools/join_report.py > informe-completo.md
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = ['README.md', 'capitulo-1.md', 'capitulo-2.md', 'capitulo-3.md', 'capitulo-4.md',
         'capitulo-5.md', 'capitulo-6.md', 'cierre.md']
NAV = re.compile(r'\n?<!-- nav:start -->.*?<!-- nav:end -->\n?', re.S)
NAMES = '|'.join(re.escape(f) for f in FILES)


def join():
    parts = []
    for f in FILES:
        text = NAV.sub('\n', (ROOT / f).read_text(encoding='utf-8')).strip('\n')
        parts.append(text)
    doc = '\n\n'.join(parts) + '\n'
    return re.sub(r'(href="|\]\()(?:' + NAMES + r')#', r'\1#', doc)


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stdout.write(join())
