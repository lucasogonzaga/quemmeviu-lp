(function () {
  var N = 7, atual = 0;
  var img = document.getElementById('tela');
  var prev = document.getElementById('prev');
  var next = document.getElementById('next');
  var dots = document.getElementById('dots');
  function src(i) { return 'telas/tela-0' + (i + 1) + '.png'; }
  var pontos = [];
  for (var i = 0; i < N; i++) { var d = document.createElement('i'); dots.appendChild(d); pontos.push(d); new Image().src = src(i); }
  function mostrar(i) {
    if (i < 0 || i >= N || i === atual) return;
    atual = i;
    img.classList.add('fade');
    setTimeout(function () {
      img.src = src(i);
      img.alt = 'Tela ' + (i + 1) + ' de ' + N;
      img.classList.remove('fade');
    }, 160);
    atualizar();
  }
  function atualizar() {
    prev.disabled = atual === 0;
    next.disabled = atual === N - 1;
    pontos.forEach(function (p, k) { p.className = k === atual ? 'on' : ''; });
  }
  prev.addEventListener('click', function () { mostrar(atual - 1); });
  next.addEventListener('click', function () { mostrar(atual + 1); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowRight' || e.key === 'PageDown') mostrar(atual + 1);
    else if (e.key === 'ArrowLeft' || e.key === 'PageUp') mostrar(atual - 1);
    else if (e.key === 'Home') mostrar(0);
    else if (e.key === 'End') mostrar(N - 1);
  });
  atualizar();
})();
