function iniciar() {
  let resultado = window.document.getElementById('resultado')
  let numero1 = Number(window.prompt(`Digite um número:`))
  let numero2 = Number(window.prompt(`Digite outro número:`))
  let mensagem

  if (numero1 > numero2) {
    mensagem = `o maior valor é <span>${numero1}</span>`
  }
  else if (numero1 < numero2) {
    mensagem = `o maior valor é <span>${numero2}</span>`
  }
  else {
    mensagem = `ambos são <span>IGUAIS</span>`
  }

  resultado.innerHTML = `<p>Analisando os valores <mark>${numero1}</mark> e <mark>${numero2}</mark>, ${mensagem}!</p>`
}
