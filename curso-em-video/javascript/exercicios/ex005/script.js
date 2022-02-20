window.alert('Seja bem-vindo(a) ao meu site!')

function calcular() {
  let numero = Number(window.prompt('Digite um número:').replace(",", "."))
  let resultado = window.document.getElementById('resultado')
  
  let dobro = (numero * 2).toLocaleString('pt-BR')
  let metade = (numero / 2).toLocaleString('pt-BR')
  numero = (numero).toLocaleString('pt-BR')

  resultado.innerHTML = `O dobro de <span>${numero}</span> é ${dobro} e a metade é ${metade}!`
}
