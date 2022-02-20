function calcular() {
  let resultado = document.getElementById('resultado')
  
  let nome = prompt('Qual é o nome do aluno?')
  let nota1 = Number(prompt(`Primeira nota de ${nome}:`).replace(',','.'))
  let nota2 = Number(prompt(`Segunda nota de ${nome}:`).replace(',','.'))

  let media = (nota1 + nota2) / 2

  resultado.innerHTML = `<h2>Analisando a situação de <span>${nome}</span></h2>`
  resultado.innerHTML += `<p>Com as notas <span>${nota1.toLocaleString('pt-BR')}</span> e <span>${nota2.toLocaleString('pt-BR')}</span> a média é <mark>${media.toLocaleString('pt-BR')}</mark>.</p>`

  if (nota1 >= 0 || nota2 >= 0) {
    if (media < 3) {
      resultado.innerHTML += `<p>Com média abaixo de 3,0 o aluno está <mark class="danger">REPROVADO(A)</mark>!</p>`
    }
    else if (media > 6) {
      resultado.innerHTML += `<p>Com média acima de 6,0 o aluno está <mark class="success">APROVADO(A)</mark>!</p>`
    }
    else {
      resultado.innerHTML += `<p>Com média entre 3,0 e 6,0 o aluno está em <mark class="warning">RECUPERAÇÃO</mark>!</p>`
    }
  }
  else {
    resultado.innerHTML += `<p>Nota não pode ser negativa!</p>`
  }
}
