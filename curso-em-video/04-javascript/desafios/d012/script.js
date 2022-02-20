function verificar() {
  let resultado = document.getElementById('resultado')
  let anterior = Number(prompt('Qual era o preço anterior do produto?').replace(',','.'))
  let atual = Number(prompt('Qual é o preço atual do produto?').replace(',','.'))
  let mensagem, precoMsg, precoPorc
  let preco
  let porcentagem
  
  if (anterior <= 0 || atual <= 0) {
    resultado.innerHTML = `<p>Por favor, digite um número <strong>maior do que 0</strong>.</p>`
  }
  else if (anterior == atual) {
    resultado.innerHTML = `<h2>Analisando os valores informados</h2>`
    resultado.innerHTML += `<p>O produto custava <strong>${anterior.toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'})}</strong> e agora custa <strong>${atual.toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'})}</strong>.</p>`
    resultado.innerHTML += `<p>Hoje o produto está <span>o mesmo preço</span>.</p>`
    resultado.innerHTML += `<p>O preço <strong>está igual</strong> em relação ao preço anterior.</p>`
    resultado.innerHTML += `<p>Uma variação de <mark>0%</mark>.</p>`
  }
  else {
    if (anterior > atual) {
      mensagem = `mais barato`
      preco = anterior - atual
      precoMsg = `caiu`
      precoPorc = `pra baixo`
      porcentagem = ((anterior - atual) / anterior / 0.01).toFixed(1)
    }
    else if (anterior < atual) {
      mensagem = `mais caro`
      preco = atual - anterior
      precoMsg = `subiu`
      precoPorc = `pra cima`
      porcentagem = ((atual - anterior) / anterior / 0.01).toFixed(1)
    }

    anterior = anterior.toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'})
    atual = atual.toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'})
    preco = preco.toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'})
    porcentagem = porcentagem.toLocaleString('pt-BR')

    resultado.innerHTML = `<h2>Analisando os valores informados</h2>`
    resultado.innerHTML += `<p>O produto custava <strong>${anterior}</strong> e agora custa <strong>${atual}</strong>.</p>`
    resultado.innerHTML += `<p>Hoje o produto está <span>${mensagem}</span>.</p>`
    resultado.innerHTML += `<p>O preço <strong>${precoMsg} ${preco}</strong> em relação ao preço anterior.</p>`
    resultado.innerHTML += `<p>Uma variação de <mark>${porcentagem}%</mark> ${precoPorc}.</p>`
  }
}
