function reajustar() {
  let resultado = document.getElementById('resultado')
  
  let nome = prompt('Qual é o nome do funcionário?')
  let salario = Number(prompt(`Qual é o salário de ${nome}?`).replace(',','.'))
  let porcentagem = Number(prompt(`O salário de ${nome} será reajustado em qual porcentagem?`).replace(',','.'))

  let aumento = salario * porcentagem / 100
  let novoSalario = salario + aumento

  if (salario < 0 && porcentagem < 0) {
    resultado.innerHTML = `<p>Salário e porcentagem de aumento devem ser <strong>maiores que 0</strong>.</p>`
  }
  else {
    salario = salario.toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'})
    aumento = aumento.toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'})
    novoSalario = novoSalario.toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'})

    resultado.innerHTML = `<h2><strong>${nome}</strong> recebeu um aumento salarial!</h2>`
    resultado.innerHTML += `<p>O salário atual era <strong>${salario}</strong>.</p>`
    resultado.innerHTML += `<p>Com aumento de <strong>${porcentagem}</strong>%, o salário aumentará <strong>${aumento}</strong> no próximo mês.</p>`
    resultado.innerHTML += `<p>E, a partir daí, <strong>${nome}</strong> passará a ganhar <span>${novoSalario}</span>!</p>`
  }
}
