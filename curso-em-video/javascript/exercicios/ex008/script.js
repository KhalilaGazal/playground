function calcular() {
  let numero = Number(window.prompt('Digite um número:').replace(",", "."))
  let resultado = window.document.getElementById('resultado')

  let absoluto = (Math.abs(numero)).toLocaleString('pt-BR')
  let inteiro = (Math.trunc(numero)).toLocaleString('pt-BR')
  let inteiroProximo = (Math.round(numero)).toLocaleString('pt-BR')
  let raizQuadrada = (Math.sqrt(numero)).toLocaleString('pt-BR')
  let raizCubica = (Math.cbrt(numero)).toLocaleString('pt-BR')
  let quadrado = (Math.pow(numero, 2)).toLocaleString('pt-BR')
  let cubico = (Math.pow(numero, 3)).toLocaleString('pt-BR')
  numero = (numero).toLocaleString('pt-BR')

  resultado.innerHTML = `<p>O número a ser analisado aqui será o <span><strong>${numero}</strong></span>.</p><hr>`
  resultado.innerHTML += `<p>- O seu valor absoluto é ${absoluto}</p>`
  resultado.innerHTML += `<p>- A sua parte inteira é ${inteiro}</p>`
  resultado.innerHTML += `<p>- O valor inteiro mais próximo é ${inteiroProximo}</p>`
  resultado.innerHTML += `<p>- A sua raiz quadrada é ${raizQuadrada}</p>`
  resultado.innerHTML += `<p>- A sua raiz cúbica é ${raizCubica}</p>`
  resultado.innerHTML += `<p>- O valor de ${numero}² é ${quadrado}</p>`
  resultado.innerHTML += `<p>- O valor de ${numero}³ é ${cubico}</p>`
}
