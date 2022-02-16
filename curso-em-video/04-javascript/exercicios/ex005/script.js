window.alert('Seja bem-vindo(a) ao meu site!')

function calcular() {
  let numero = Number(window.prompt('Digite um número:'))
  let resultado = window.document.getElementById('resultado')
  
  let dobro = numero * 2
  let metade = numero / 2

  resultado.innerHTML = `O dobro de ${numero} é ${dobro} e a metade é ${metade}!`
}