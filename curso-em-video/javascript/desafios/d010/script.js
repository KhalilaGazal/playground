function calcular() {
  let resultado = document.getElementById('resultado')
  
  let a = Number(prompt(`Qual é o valor de a?`).replace(',','.'))
  let b = Number(prompt(`Qual é o valor de b?`).replace(',','.'))
  let c = Number(prompt(`Qual é o valor de c?`).replace(',','.'))

  let equacao = `${a}x² + ${b}x + ${c} = 0`
  let calculo = `Δ = ${b}² - 4 . ${a} . ${c}`
  delta = (b ** 2) - 4 * a * c

  resultado.innerHTML = '<h2>Resolvendo Bhaskara</h2>'
  resultado.innerHTML += `<p>A equação atual é <strong>${equacao}</strong></p>`
  resultado.innerHTML += `<p>O cálculo realizado será <strong>${calculo}</strong></p>`
  resultado.innerHTML += `<p>O valor calculado foi <mark>Δ = ${delta}</mark></p>`
}
