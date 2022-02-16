function acao() {
  let nome = window.prompt('Qual é o seu nome?')
  let resultado = window.document.getElementById('resultado')
  
  resultado.innerHTML = `Olá, <strong>${nome}</strong>! É um grande prazer te conhecer! 🖖`
}