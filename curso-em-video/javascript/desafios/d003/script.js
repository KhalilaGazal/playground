function calcular() {
  let numero = Number(prompt('Digite um número inteiro qualquer:'))
  let antecessor = numero - 1
  let sucessor = numero + 1
  alert(`Antes de ${numero}, temos o número ${antecessor}.\nDepois de ${numero}, temos o número ${sucessor}.`)
}
