function iniciar() {
  let resultado = window.document.getElementById('resultado')
  let numero = Number(window.prompt(`Digite um número:`))
  let mensagem

  if (numero % 2 == 0) {
    mensagem = 'PAR'
  }
  else {
    mensagem = 'ÍMPAR'
  }

  resultado.innerHTML = `<p>O número <strong>${numero}</strong> que foi digitado é <span>${mensagem}</span>!</p>`
}
