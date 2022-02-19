window.alert('Seja bem-vindo(a) ao meu site!')

function calcular() {
  let numero = Number(window.prompt('Digite um número:'))
  let resultado = window.document.getElementById('resultado')
  
  let dobro = String(numero * 2).replace('.', ',')
  let metade = String(numero / 2).replace('.', ',')
  numero = String(numero).replace('.', ',')

  resultado.innerHTML = `O dobro de <span>${numero}</span> é ${dobro} e a metade é ${metade}!`
}
