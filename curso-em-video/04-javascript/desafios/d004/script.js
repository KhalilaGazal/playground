function calcular() {
  let produto = prompt('Qual é o nome do produto que você está comprando?')
  let preco = Number(prompt(`Quanto custa "${produto}" que você está comprando?`))
  let pago = Number(prompt(`Qual é o valor dado para pagar "${produto}"?`))
  let troco = pago - preco
  let trocoAbs = Math.abs(troco)
  let valorProduto = preco.toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'})
  let valorPago = pago.toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'})
  let valorTroco = troco.toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'})
  let valorTrocoAbs = trocoAbs.toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'})
  if (troco >= 0) {
    alert(`Você comprou "${produto}" que custou ${valorProduto}.\nDeu ${valorPago} em dinheiro e vai receber ${valorTroco}.\n\nVolte sempre!`)
  }
  else {
    alert(`Você comprou "${produto}" que custou ${valorProduto}.\nDeu ${valorPago} em dinheiro e está faltando ${valorTrocoAbs}.`)
  }
}
