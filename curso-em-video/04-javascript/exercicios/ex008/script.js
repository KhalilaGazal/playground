function calcular() {
  let numero = Number(window.prompt('Digite um número:'))
  let resultado = window.document.getElementById('resultado')

  let absoluto = String(Math.abs(numero)).replace('.', ',')
  let inteiro = Math.trunc(numero)
  let inteiroProximo = Math.round(numero)
  let raizQuadrada = String(Math.sqrt(numero)).replace('.', ',')
  let raizCubica = String(Math.cbrt(numero)).replace('.', ',')
  let quadrado = String(Math.pow(numero, 2)).replace('.', ',')
  let cubico = String(Math.pow(numero, 3)).replace('.', ',')
  numero = String(numero).replace('.', ',')

  resultado.innerHTML = `<p>O número a ser analisado aqui será o <span><strong>${numero}</strong></span>.</p><hr>`
  resultado.innerHTML += `<p>- O seu valor absoluto é ${absoluto}</p>`
  resultado.innerHTML += `<p>- A sua parte inteira é ${inteiro}</p>`
  resultado.innerHTML += `<p>- O valor inteiro mais próximo é ${inteiroProximo}</p>`
  resultado.innerHTML += `<p>- A sua raiz quadrada é ${raizQuadrada}</p>`
  resultado.innerHTML += `<p>- A sua raiz cúbica é ${raizCubica}</p>`
  resultado.innerHTML += `<p>- O valor de ${numero}² é ${quadrado}</p>`
  resultado.innerHTML += `<p>- O valor de ${numero}³ é ${cubico}</p>`
}
