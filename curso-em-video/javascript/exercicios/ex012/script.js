function iniciar() {
  let resultado = window.document.getElementById('resultado')
  let numero = Number(window.prompt(`Digite um número:`).replace(',','.'))
  let mensagem

  if (numero % 1 != 0 && !isNaN(numero % 1)) {
    resultado.innerHTML = `<p>Por favor, digite um número <strong>inteiro</strong>.</p>`
  }
  else {
    if (numero % 2 == 0) {
      mensagem = 'PAR'
    }
    else {
      mensagem = 'ÍMPAR'
    }
  
    resultado.innerHTML = `<p>O número <strong>${numero}</strong> que foi digitado é <span>${mensagem}</span>!</p>`
  }    
}
