/* js/data/core.js: контейнеры данных курса. Подключается ПЕРВЫМ среди файлов js/data/.
   ДАННЫЕ курса лежат в js/data/*, логика и интерфейс — в js/app.js (подключается ПОСЛЕ всех данных).
   U  — юниты и повторения: каждый файл js/data/units/<id>.js делает U.push({...}); порядок в U = порядок тегов script в index.html.
   TB — банк заданий: каждый файл js/data/bank/<id юнита>.js делает TB.push(...).
   Дальше: units-finish.js (id и метки), levels.js (PL), reference.js (ref0), glossary.js (G).
   Новый юнит: файл units/<id>.js + строка script в index.html ПЕРЕД units-finish.js; банк юнита: файл bank/<id>.js. */
var U=[];
var TB=[];
