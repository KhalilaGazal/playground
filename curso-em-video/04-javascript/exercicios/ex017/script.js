let resultado = window.document.getElementById('resultado')

function gerarNumero() {
  let min = 1
  let max = 100
  let numero = Math.trunc(Math.random() * (max - min) + min)

  resultado.innerHTML += `<p>Acabei de pensar no número <mark>${numero}</mark>!</p>`
}

function limpar () {
  resultado.innerHTML = null
}