/* units-finish.js: после всех юнитов присваивает уровень l, id (a1-u01, a1-r1…) и метки заданий (u, l, s, d). Подключается после всех файлов units/. */
U.forEach(function(u){u.l=u.l||((u.t.match(/^(A1|A2|B1|B2)/)||[])[1])||"A1"});
var _n=0;U.forEach(function(u){u.id=u.r?u.l.toLowerCase()+"-r"+u.r:u.l.toLowerCase()+"-u"+("0"+(++_n)).slice(-2);u.q.forEach(function(q){q.u=u.id;q.l=u.l;q.s=q.s||"gr";q.d=q.d||(q.t?2:1)})});
