function calcular() {
  let resultado = window.document.getElementById('resultado')
  let anoNasc = Number(window.prompt('Em que ano você nasceu?'))
  
  let data = new Date()
  let anoAtual = data.getFullYear()

  let idade = anoAtual - anoNasc

  console.log(anoAtual)

  if (anoNasc <= 1900) {
    resultado.innerHTML = `<p>Por favor, digite um ano maior que 1900.</p>`
  }
  else if (anoNasc > anoAtual) {
    resultado.innerHTML = `<p>Por favor, digite um ano menor que ${anoAtual}.</p>`
  }
  else {
    resultado.innerHTML = `<p>Quem nasceu em <strong>${anoNasc}</strong> vai completar <span>${idade}</span> ano(s) em <strong>${anoAtual}</strong>.`
  }
}
