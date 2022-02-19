function calcular() {
  let nome = window.prompt('Qual é o nome do aluno?')
  let nota1 = Number(window.prompt(`Qual foi a primeira nota de ${nome}?`).replace(",", "."))
  let nota2 = Number(window.prompt(`Além de ${nota1} qual foi a outra nota de ${nome}?`).replace(",", "."))
  let resultado = window.document.getElementById('resultado')
  
  let media = (nota1 + nota2) / 2

  media = media.toLocaleString('pt-BR')
  nota1 = nota1.toLocaleString('pt-BR')
  nota2 = nota2.toLocaleString('pt-BR')

  resultado.innerHTML = `<p>Calculando a média final de <span>${nome}</span>.</p>`
  resultado.innerHTML += `<p>As notas obtidas foram <mark>${nota1}</mark> e <mark>${nota2}</mark>.</p>`
  resultado.innerHTML += `<p>A média final será <mark>${media}</mark>.</p>`
}
