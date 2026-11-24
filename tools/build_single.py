#!/usr/bin/env python3
"""Собирает ОДИН автономный HTML из index.html + css/styles.css + всех js/*, перечисленных тегами <script src=...> в index.html (в том же порядке).
Зачем: (1) скрипты проверки course-qa-gate и ru-legal-content-guard принимают один файл;
(2) единый файл можно отдать человеку «скачай и открой» или положить на флешку.
Запуск из корня репозитория:  python3 tools/build_single.py [выходной_файл]
По умолчанию пишет dist/engladder_single.html (папка dist в репозиторий не коммитится)."""
import sys, os, re
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rd = lambda p: open(os.path.join(root, p), encoding='utf-8').read()
html = rd('index.html')
link = '<link rel="stylesheet" href="css/styles.css">'
assert html.count(link) == 1, 'index.html изменён: проверьте подключение css'
html = html.replace(link, '<style>' + rd('css/styles.css') + '</style>')
tag = re.compile(r'<script src="([^"]+)"></script>')
ms = list(tag.finditer(html))
assert ms, 'в index.html нет тегов <script src=...>'
code = '\n'.join(rd(m.group(1)) for m in ms)
assert '</script' not in code, 'в JS встретилось </script: сборка сломает страницу'
html = html[:ms[0].start()] + '<script>' + code + '</script>' + html[ms[-1].end():]
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(root, 'dist', 'engladder_single.html')
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, 'w', encoding='utf-8').write(html)
print('Собрано:', out, len(html.encode('utf-8')), 'байт; скриптов:', len(ms))
