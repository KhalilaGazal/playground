let resultado = window.document.getElementById('resultado')
let clique = 0

function contar() {
  clique++;
  resultado.innerHTML = `<p>O contador está com <mark>${clique}</mark> cliques.</p>`
}

function zerar() {
  clique = 0
  resultado.innerHTML = ''
}