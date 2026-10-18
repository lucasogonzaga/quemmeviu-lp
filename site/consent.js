/* Gestão de cookies da LP Quem Me Viu (LGPD).
 * Nada de terceiros carrega antes do consentimento. Categorias:
 *   necessarios (sempre ativo) · desempenho (Google Tag Manager, Microsoft Clarity) · publicidade (Google Ads)
 * A escolha fica em localStorage ("qmv_consent"). Reabrir: link com href="#cookies" ou window.qmvCookies.open().
 * A conversão do Google Ads (clique no WhatsApp) só dispara com consentimento de publicidade.
 * Novas tags: carregue-as dentro de applyConsent() e libere os domínios na CSP (deploy/setup-server.sh). */
(function () {
  'use strict';
  var KEY = 'qmv_consent';
  var VERSION = 1;
  var IDS = { gtm: 'GTM-PDDHV4PK', ads: 'AW-18517888153', clarity: 'wx9mphq0ba' };
  var WHATSAPP_CONVERSION = 'AW-18517888153/cGW-CImzjaAdEJmZgv5E'; // Google Ads: clique no WhatsApp
  var POLICY_URL = 'politica-de-privacidade.html';

  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  gtag('consent', 'default', { ad_storage: 'denied', analytics_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied' });

  var loaded = { gtm: false, ads: false, clarity: false };

  function read() {
    try {
      var c = JSON.parse(localStorage.getItem(KEY));
      if (c && c.v === VERSION) return c;
    } catch (e) {}
    return null;
  }
  function write(perf, ads) {
    var c = { v: VERSION, t: new Date().toISOString(), perf: !!perf, ads: !!ads };
    try { localStorage.setItem(KEY, JSON.stringify(c)); } catch (e) {}
    return c;
  }
  function addScript(src) {
    var s = document.createElement('script');
    s.async = true; s.src = src;
    document.head.appendChild(s);
  }

  function applyConsent(c) {
    gtag('consent', 'update', {
      analytics_storage: c.perf ? 'granted' : 'denied',
      ad_storage: c.ads ? 'granted' : 'denied',
      ad_user_data: c.ads ? 'granted' : 'denied',
      ad_personalization: c.ads ? 'granted' : 'denied'
    });
    if ((c.perf || c.ads) && !loaded.gtm) {
      loaded.gtm = true;
      window.dataLayer.push({ 'gtm.start': Date.now(), event: 'gtm.js' });
      addScript('https://www.googletagmanager.com/gtm.js?id=' + IDS.gtm);
    }
    if (c.ads && !loaded.ads) {
      loaded.ads = true;
      addScript('https://www.googletagmanager.com/gtag/js?id=' + IDS.ads);
      gtag('js', new Date());
      gtag('config', IDS.ads);
    }
    if (c.perf && !loaded.clarity) {
      loaded.clarity = true;
      (function (c2, l, a, r, i) {
        c2[a] = c2[a] || function () { (c2[a].q = c2[a].q || []).push(arguments); };
        var t = l.createElement(r); t.async = 1; t.src = 'https://www.clarity.ms/tag/' + i;
        var y = l.getElementsByTagName(r)[0]; y.parentNode.insertBefore(t, y);
      })(window, document, 'clarity', 'script', IDS.clarity);
    }
    window.dataLayer.push({ event: 'consent_update', consent_performance: !!c.perf, consent_ads: !!c.ads });
  }

  /* ---------- interface ---------- */
  var CSS = '' +
    '.qmvc,.qmvc *{box-sizing:border-box}' +
    '.qmvc{font-family:"DM Sans",system-ui,sans-serif;color:#eef3f7;line-height:1.5}' +
    '.qmvc-banner{position:fixed;z-index:2147483000;right:20px;bottom:20px;width:min(440px,calc(100vw - 32px));padding:22px;border-radius:22px;background:linear-gradient(160deg,#172a66,#10215a);border:1px solid rgba(79,245,154,.35);box-shadow:0 24px 60px -12px rgba(0,0,0,.6),0 0 30px rgba(79,245,154,.12)}' +
    '.qmvc-banner p{margin:0 0 14px;font-size:14px;color:#dce5ec}' +
    '.qmvc a{color:#4ff59a;text-decoration:underline}' +
    '.qmvc-row{display:flex;flex-direction:column;gap:10px}' +
    '.qmvc-btn{appearance:none;cursor:pointer;border-radius:999px;padding:12px 18px;font:700 14px "DM Sans",system-ui,sans-serif;border:1.5px solid #4ff59a;text-align:center}' +
    '.qmvc-btn:focus-visible,.qmvc a:focus-visible,.qmvc-sw:focus-visible{outline:3px solid #9dffc6;outline-offset:2px}' +
    '.qmvc-pri{background:#4ff59a;color:#06120b}.qmvc-pri:hover{background:#9dffc6}' +
    '.qmvc-sec{background:transparent;color:#eef3f7;border-color:rgba(238,243,247,.55)}.qmvc-sec:hover{border-color:#4ff59a;color:#4ff59a}' +
    '.qmvc-lnk{background:none;border:0;padding:0;color:#4ff59a;text-decoration:underline;font:500 13px "DM Sans",system-ui,sans-serif;cursor:pointer;margin-bottom:14px;display:inline-block}' +
    '.qmvc-ov{position:fixed;inset:0;z-index:2147483001;background:rgba(5,12,38,.72);display:flex;align-items:center;justify-content:center;padding:16px}' +
    '.qmvc-modal{width:min(560px,100%);max-height:calc(100vh - 32px);overflow:auto;padding:26px;border-radius:24px;background:linear-gradient(160deg,#172a66,#0d1d4f);border:1px solid rgba(79,245,154,.35)}' +
    '.qmvc-modal h2{margin:0 0 6px;font:800 20px Sora,system-ui,sans-serif;letter-spacing:-.01em}' +
    '.qmvc-modal>p{margin:0 0 18px;font-size:14px;color:#b9c6d2}' +
    '.qmvc-cat{display:flex;align-items:flex-start;justify-content:space-between;gap:16px;padding:14px 0;border-top:1px solid rgba(255,255,255,.12)}' +
    '.qmvc-cat b{display:block;font:700 15px "DM Sans",system-ui,sans-serif}.qmvc-cat span{font-size:13px;color:#b9c6d2}' +
    '.qmvc-on{font-size:13px;font-weight:700;color:#4ff59a;white-space:nowrap;padding-top:2px}' +
    '.qmvc-sw{appearance:none;flex:none;width:46px;height:26px;border-radius:999px;border:0;background:#3a4a7a;position:relative;cursor:pointer;transition:background .15s}' +
    '.qmvc-sw::after{content:"";position:absolute;top:3px;left:3px;width:20px;height:20px;border-radius:50%;background:#fff;transition:transform .15s}' +
    '.qmvc-sw[aria-checked="true"]{background:#4ff59a}.qmvc-sw[aria-checked="true"]::after{transform:translateX(20px);background:#06120b}' +
    '.qmvc-acts{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px;padding-top:18px;border-top:1px solid rgba(255,255,255,.12)}' +
    '.qmvc-acts .qmvc-btn{flex:1 1 150px}' +
    '@media (max-width:520px){.qmvc-banner{right:16px;left:16px;bottom:16px;width:auto}}' +
    '@media (prefers-reduced-motion:reduce){.qmvc-sw,.qmvc-sw::after{transition:none}}';

  var root, banner, overlay, lastFocus;

  function el(tag, attrs, html) {
    var n = document.createElement(tag);
    for (var k in attrs) n.setAttribute(k, attrs[k]);
    if (html) n.innerHTML = html;
    return n;
  }
  function ensureRoot() {
    if (root) return;
    root = el('div', { 'class': 'qmvc' });
    root.appendChild(el('style', {}, CSS));
    document.body.appendChild(root);
  }
  function closeAll() {
    if (banner) { banner.remove(); banner = null; }
    if (overlay) { overlay.remove(); overlay = null; }
    document.removeEventListener('keydown', onKey);
    if (lastFocus && lastFocus.focus) { try { lastFocus.focus(); } catch (e) {} }
  }
  function choose(perf, ads) {
    var c = write(perf, ads);
    closeAll();
    applyConsent(c);
  }
  function onKey(e) { if (e.key === 'Escape' && overlay) { overlay.remove(); overlay = null; if (!read()) showBanner(); } }

  function showBanner() {
    ensureRoot();
    if (banner) return;
    banner = el('div', { 'class': 'qmvc-banner', role: 'dialog', 'aria-live': 'polite', 'aria-label': 'Aviso de cookies' },
      '<p>Utilizamos cookies para auxiliar a sua navegação em nosso sítio eletrônico e melhorar nossos serviços. ' +
      'Ao clicar em “Aceitar todos os cookies”, você concorda com o uso descrito. Você também pode rejeitar todos os cookies não necessários. ' +
      'Saiba mais na <a href="' + POLICY_URL + '">Política de Privacidade</a>.</p>' +
      '<button type="button" class="qmvc-lnk" data-a="defs">Definições de cookies</button>' +
      '<div class="qmvc-row">' +
      '<button type="button" class="qmvc-btn qmvc-pri" data-a="all">Aceitar todos os cookies</button>' +
      '<button type="button" class="qmvc-btn qmvc-sec" data-a="none">Rejeitar cookies não necessários</button>' +
      '</div>');
    banner.addEventListener('click', function (e) {
      var a = e.target && e.target.getAttribute && e.target.getAttribute('data-a');
      if (a === 'all') choose(true, true);
      else if (a === 'none') choose(false, false);
      else if (a === 'defs') openModal();
    });
    root.appendChild(banner);
  }

  function sw(id, on, label) {
    return '<button type="button" role="switch" class="qmvc-sw" id="' + id + '" aria-checked="' + (on ? 'true' : 'false') + '" aria-label="' + label + '"></button>';
  }
  function openModal() {
    ensureRoot();
    lastFocus = document.activeElement;
    if (banner) { banner.remove(); banner = null; }
    if (overlay) overlay.remove();
    var cur = read() || { perf: false, ads: false };
    overlay = el('div', { 'class': 'qmvc-ov' });
    overlay.innerHTML =
      '<div class="qmvc-modal" role="dialog" aria-modal="true" aria-labelledby="qmvc-t">' +
      '<h2 id="qmvc-t">Configuração de cookies</h2>' +
      '<p>Escolha quais categorias você autoriza. Você pode mudar sua escolha quando quiser, em “Definições de cookies” no rodapé. Detalhes na <a href="' + POLICY_URL + '">Política de Privacidade</a>.</p>' +
      '<div class="qmvc-cat"><div><b>Cookies necessários</b><span>Essenciais para o site funcionar e para lembrar a sua escolha de cookies. Não podem ser desativados.</span></div><div class="qmvc-on">Sempre ativos</div></div>' +
      '<div class="qmvc-cat"><div><b>Cookies de desempenho</b><span>Medem como o site é usado (páginas visitadas, erros, tempo de navegação) para melhorarmos a experiência. Ferramentas: Google Tag Manager e Microsoft Clarity.</span></div>' + sw('qmvc-perf', cur.perf, 'Cookies de desempenho') + '</div>' +
      '<div class="qmvc-cat"><div><b>Cookies de publicidade</b><span>Medem a eficácia dos anúncios e permitem mostrar publicidade mais relevante. Ferramenta: Google Ads.</span></div>' + sw('qmvc-ads', cur.ads, 'Cookies de publicidade') + '</div>' +
      '<div class="qmvc-acts">' +
      '<button type="button" class="qmvc-btn qmvc-pri" data-a="all">Permitir todos</button>' +
      '<button type="button" class="qmvc-btn qmvc-sec" data-a="save">Salvar</button>' +
      '<button type="button" class="qmvc-btn qmvc-sec" data-a="none">Rejeitar cookies não necessários</button>' +
      '</div></div>';
    overlay.addEventListener('click', function (e) {
      var t = e.target;
      if (t === overlay) { overlay.remove(); overlay = null; if (!read()) showBanner(); return; }
      if (t.getAttribute && t.getAttribute('role') === 'switch') {
        t.setAttribute('aria-checked', t.getAttribute('aria-checked') === 'true' ? 'false' : 'true'); return;
      }
      var a = t.getAttribute && t.getAttribute('data-a');
      if (a === 'all') choose(true, true);
      else if (a === 'none') choose(false, false);
      else if (a === 'save') choose(
        document.getElementById('qmvc-perf').getAttribute('aria-checked') === 'true',
        document.getElementById('qmvc-ads').getAttribute('aria-checked') === 'true');
    });
    root.appendChild(overlay);
    document.addEventListener('keydown', onKey);
    var first = overlay.querySelector('.qmvc-pri'); if (first) first.focus();
  }

  window.qmvCookies = { open: openModal };

  document.addEventListener('click', function (e) {
    var a = e.target && e.target.closest && e.target.closest('a[href="#cookies"],[data-cookie-settings]');
    if (a) { e.preventDefault(); openModal(); return; }
    var w = e.target && e.target.closest && e.target.closest('a[href*="wa.me/"]');
    if (w) {
      window.dataLayer.push({ event: 'whatsapp_click' });
      var c = read();
      if (c && c.ads) gtag('event', 'conversion', { send_to: WHATSAPP_CONVERSION });
    }
  });

  function init() {
    var c = read();
    if (c) applyConsent(c); else showBanner();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
