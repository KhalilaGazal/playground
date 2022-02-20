let cotacao

function pegarCotacao() {
  cotacao = Number(prompt('Antes de mais nada: quanto está a cotação do dólar agora?').replace(',','.'))
}

function converter() {
  let resultado = document.getElementById('resultado')
  let brl = Number(prompt('Quantos R$ você tem na carteira?').replace(',','.'))
  let usd = brl / cotacao
  brl = brl.toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'})
  usd = usd.toLocaleString('pt-BR', {style: 'currency', currency: 'USD'})
  resultado.innerHTML = `${brl} = ${usd}`
}
