function calcular() {
  let resultado = document.getElementById('resultado')
  let produto = prompt('Qual é o nome do produto que você está comprando?')
  let preco = Number(prompt(`Qual é o preço de "${produto}"?`).replace(',','.'))
  let porcentagem = 10
  let porcento = porcentagem / 100
  let desconto = preco * porcento
  let novoPreco = preco - desconto

  if (preco <= 0) {
    resultado.innerHTML = '<p>Por favor, digite um preço <strong>maior que 0</strong>!</p>'
  }
  else {
    preco = preco.toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'})
    desconto = desconto.toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'})
    novoPreco = novoPreco.toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'})

    resultado.innerHTML = `<h2>Calculando <strong>${porcentagem}%</strong></h2>`
    resultado.innerHTML += `<p>O preço original era <strong>${preco}</strong>.</p>`
    resultado.innerHTML += `<p>Você acaba de ganhar <strong>${desconto}</strong> de desconto (-<strong>${porcentagem}</strong>%).</p>`
    resultado.innerHTML += `<p>No fim, você pagará <span>${novoPreco}</span> no produto <strong>${produto}</strong>!</p>`
  }
}
