function calcular() {
  let resultado = window.document.getElementById('resultado')
  let anoNasc = Number(window.prompt('Em que ano você nasceu?'))
  
  let data = new Date()
  let anoAtual = data.getFullYear()

  let idade = anoAtual - anoNasc

  resultado.innerHTML = `<p>Quem nasceu em ${anoNasc} vai completar <strong>${idade}</strong> anos em ${anoAtual}.`
}