let vetor = []
let soma = 0
let select = document.getElementById('select')
let resultado = document.getElementById('resultado')

function adicionar() {
  let numero = Number(document.getElementById('numero').value)
  let item = document.createElement('option')

  if (numero < 1 || numero > 100) {
    alert('Valor inválido!')
  }
  else if (vetor.indexOf(numero) != -1) {
    alert('Valor já encontrado na lista!')
  }
  else {
    resultado.innerHTML = ''

    vetor.push(numero)
    soma += numero

    item.value = `valor${numero}`
    item.text = `Valor ${numero} adicionado.`
    select.appendChild(item)
  }  
}

function finalizar() {
  let qtd = vetor.length

  if (qtd == 0) {
    alert('Adicione valores antes de finalizar!')
  }
  else {
    let media = soma / qtd
    let menor = Math.min(...vetor)
    let maior = Math.max(...vetor)
  
    resultado.innerHTML = `<p>Ao todo, temos ${qtd} números cadastrados.</p>`
    resultado.innerHTML += `<p>O maior valor informado foi ${maior}.</p>`
    resultado.innerHTML += `<p>O menor valor informado foi ${menor}.</p>`
    resultado.innerHTML += `<p>Somando todos os valores, temos ${soma}.</p>`
    resultado.innerHTML += `<p>A média dos valores digitados é ${media}.</p>`
  }  
}

function limpar() {
  resultado.innerHTML = ''
  vetor = []
  qtd = 0
  soma = 0
  maior = 0
  menor = 0

  let i, l = select.options.length - 1
  for (i = l; i >= 0; i--) {
    select.remove(i)
  }
}