function somar() {
  let numero1 = Number(window.prompt('Digite um número:'))
  let numero2 = Number(window.prompt('Digite outro número:'))
  let resultado = window.document.getElementById('resultado')
  
  let soma = String(numero1 + numero2).replace('.', ',')
  numero1 = String(numero1).replace('.', ',')
  numero2 = String(numero2).replace('.', ',')

  resultado.innerHTML = `A soma entre <mark>${numero1}</mark> e <mark>${numero2}</mark> é igual a <span>${soma}</span>!`
}
