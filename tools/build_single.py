#!/usr/bin/env python3
"""Собирает ОДИН автономный HTML из index.html + css/styles.css + js/data.js + js/app.js.
Зачем: (1) скрипты проверки course-qa-gate и ru-legal-content-guard принимают один файл;
(2) единый файл можно отдать человеку «скачай и открой» или положить на флешку.
Запуск из корня репозитория:  python3 tools/build_single.py [выходной_файл]
По умолчанию пишет dist/engladder_single.html (папка dist в репозиторий не коммитится)."""
import sys, os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rd = lambda p: open(os.path.join(root, p), encoding='utf-8').read()
html = rd('index.html')
link = '<link rel="stylesheet" href="css/styles.css">'
scr = '<script src="js/data.js"></script>\n<script src="js/app.js"></script>'
assert html.count(link) == 1 and html.count(scr) == 1, 'index.html изменён: проверьте подключение css/js'
html = html.replace(link, '<style>' + rd('css/styles.css') + '</style>')
html = html.replace(scr, '<script>' + rd('js/data.js') + '\n' + rd('js/app.js') + '</script>')
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(root, 'dist', 'engladder_single.html')
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, 'w', encoding='utf-8').write(html)
print('Собрано:', out, len(html.encode('utf-8')), 'байт')
