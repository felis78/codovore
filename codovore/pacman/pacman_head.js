window.google = {
  kEI: 'Quz2S63qIYeglAfw8oHGCg',
  kEXPI: '17259,23663,24477,24661,24745,24770,24808',
  kCSI: {
    e: '17259,23663,24477,24661,24745,24770,24808',
    ei: 'Quz2S63qIYeglAfw8oHGCg',
    expi: '17259,23663,24477,24661,24745,24770,24808'
  },
  ml: function () {
  },
  pageState: '#',
  kHL: 'en',
  time: function () {
    return (new Date).getTime()
  },
  log: function (b, d, c) {
    var a = new Image,
    e = google,
    g = e.lc,
    f = e.li;
    a.onerror = (a.onload = (a.onabort = function () {
      delete g[f]
    }));
    g[f] = a;
    c = c ||
    '/gen_204?atyp=i&ct=' + b + '&cad=' + d + '&zx=' + google.time();
    a.src = c;
    e.li = f + 1
  },
  lc: [],
  li: 0,
  j: {
    en: 1,
    l: function () {
    },
    e: function () {
    },
    b: location.hash &&
    location.hash != '#',
    bv: 3,
    pl: [],
    mc: 0,
    sc: 0.5
  },
  Toolbelt: {
  }
};
(
  function () {
    for (
      var d = 0,
      c;
      c = [
        'ad',
        'bc',
        'p',
        'pa',
        'zd',
        'ac',
        'pc',
        'pah',
        'ph',
        'sa',
        'xx',
        'zc',
        'zz'
      ][d++];
    ) (
      function (a) {
        google.j[a] = function () {
          google.j.pl.push([a,
          arguments])
        }
      }
    ) (c)
  }
) ();
window.google.sn = 'webhp';
window.google.timers = {
  load: {
    t: {
      start: (new Date).getTime()
    }
  }
};
try {
  window.google.pt = window.gtbExternal &&
  window.gtbExternal.pageT();
} catch (u) {
}
window.google.jsrt_kill = 1;
var _gjwl = location;
function _gjuc() {
  var b = _gjwl.href.indexOf('#');
  if (b >= 0) {
    var a = _gjwl.href.substring(b + 1);
    if (
      /(^|&)q=/.test(a) &&
      a.indexOf('#') == - 1 &&
      !/(^|&)cad=h($|&)/.test(a)
    ) {
      _gjwl.replace('/search?' + a.replace(/(^|&)fp=[^&]*/g, '') + '&cad=h');
      return 1
    }
  }
  return 0
}
function _gjp() {
  !(window._gjwl.hash && window._gjuc()) &&
  setTimeout(_gjp, 500)
};
google.y = {};
google.x = function (e, g) {
  google.y[e.id] = [
    e,
    g
  ];
  return false
};
if (!window.google) window.google = {};
window.google.crm = {};
window.google.cri = 0;
window.clk = function (e, f, g, k, l, b, m) {
  if (document.images) {
    var a = encodeURIComponent ||
    escape,
    c = new Image,
    h = window.google.cri++;
    window.google.crm[h] = c;
    c.onerror = (c.onload = (c.onabort = function () {
      delete window.google.crm[h]
    }));
    if (b && b.substring(0, 6) != '&sig2=') b = '&sig2=' + b;
    c.src = [
      '/url?sa=T',
      '',
      f ? '&oi=' + a(f) : '',
      g ? '&cad=' + a(g) : '',
      '&ct=',
      a(k || 'res'),
      '&cd=',
      a(l),
      '&ved=',
      a(m),
      e ? '&url=' + a(e.replace(/#.*/, '')).replace(/\+/g, '%2B') : '',
      '&ei=',
      'Quz2S63qIYeglAfw8oHGCg',
      b
    ].join('')
  }
  return true
};
window.gbar = {
  qs: function () {
  },
  tg: function (e) {
    var o = {
      id: 'gbar'
    };
    for (i in e) o[i] = e[i];
    google.x(o, function () {
      gbar.tg(o)
    })
  }
};
