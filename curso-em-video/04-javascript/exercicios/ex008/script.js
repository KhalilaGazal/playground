function calcular() {
  let numero = Number(window.prompt('Digite um número:'))
  let resultado = window.document.getElementById('resultado')

  let absoluto = Math.abs(numero)
  let inteiro = Math.trunc(numero)
  let inteiroProximo = Math.round(numero)
  let raizQuadrada = Math.sqrt(numero)
  let raizCubica = Math.cbrt(numero)
  let quadrado = Math.pow(numero, 2)
  let cubico = Math.pow(numero, 3)

  resultado.innerHTML = `<p>O número a ser analisado aqui será o <strong>${numero}</strong>.</p><hr>`
  resultado.innerHTML += `<p>O seu valor absoluto é ${absoluto}</p>`
  resultado.innerHTML += `<p>A sua parte inteira é ${inteiro}</p>`
  resultado.innerHTML += `<p>O valor inteiro mais próximo é ${inteiroProximo}</p>`
  resultado.innerHTML += `<p>A sua raiz quadrada é ${raizQuadrada}</p>`
  resultado.innerHTML += `<p>A sua raiz cúbica é ${raizCubica}</p>`
  resultado.innerHTML += `<p>O valor de ${numero}² é ${quadrado}</p>`
  resultado.innerHTML += `<p>O valor de ${numero}³ é ${cubico}</p>`
}