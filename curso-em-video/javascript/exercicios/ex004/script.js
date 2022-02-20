function acao() {
  let nome = window.prompt('Qual é o seu nome?')
  let resultado = window.document.getElementById('resultado')
  
  resultado.innerHTML = `Olá, <span>${nome}</span>!<br> É um grande prazer te conhecer! 🤙`
}
