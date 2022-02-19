function somar() {
  let numero1 = Number(window.prompt('Digite um número:').replace(",", "."))
  let numero2 = Number(window.prompt('Digite outro número:').replace(",", "."))
  let resultado = window.document.getElementById('resultado')
  
  let soma = (numero1 + numero2).toLocaleString('pt-BR')
  numero1 = (numero1).toLocaleString('pt-BR')
  numero2 = (numero2).toLocaleString('pt-BR')

  resultado.innerHTML = `A soma entre <mark>${numero1}</mark> e <mark>${numero2}</mark> é igual a <span>${soma}</span>!`
}
