function calcular() {
  let resultado = window.document.getElementById('resultado')
  let anoNasc = Number(window.prompt('Em que ano você nasceu?').replace(',','.'))
  
  let data = new Date()
  let anoAtual = data.getFullYear()

  let idade = anoAtual - anoNasc

  if (anoNasc % 1 != 0 && !isNaN(anoNasc % 1)) {
    resultado.innerHTML = `<p>Por favor, digite um número <strong>inteiro</strong>.</p>`
  }
  else {
    if (anoNasc <= 1900) {
      resultado.innerHTML = `<p>Por favor, digite um ano <strong>maior que 1900</strong>.</p>`
    }
    else if (anoNasc > anoAtual) {
      resultado.innerHTML = `<p>Por favor, digite um ano <strong>menor que ${anoAtual}</strong>.</p>`
    }
    else {
      resultado.innerHTML = `<p>Quem nasceu em <strong>${anoNasc}</strong> vai completar <span>${idade}</span> ano(s) em <strong>${anoAtual}</strong>.`
    }
  }  
}
