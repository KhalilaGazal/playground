function verificar() {
  let resultado = document.getElementById('resultado')
  let ano = Number(prompt('Qual é o ano que você quer verificar?'))
  let mensagem

  let success = String.fromCodePoint(0x2705)
  let danger = String.fromCodePoint(0x274C)

  resultado.innerHTML = `<h2>Analisando o ano de ${ano}</h2>`

  if (ano % 1 != 0 && !isNaN(ano % 1)) {
    resultado.innerHTML = `<p>Por favor, digite um número <strong>inteiro</strong>.</p>`
  }
  else {
    if (ano % 4 == 0 && ano % 100 != 0 || ano % 400 == 0) {
      mensagem = `<mark class="success">É BISSEXTO ${success}</mark>`
    }
    else {
      mensagem = `<mark class="danger">NÃO É BISSEXTO ${danger}</mark>`
    }
  }
  
  resultado.innerHTML += `<p>O ano de ${ano} ${mensagem}</p>`
}
