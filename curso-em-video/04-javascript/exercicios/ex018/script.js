let resultado = window.document.getElementById('resultado')
let btnNovoJogo = window.document.getElementById('btn-novo-jogo')
let btnAdivinhar = window.document.getElementById('btn-adivinhar')
let sorteio = 0, palpite = 0, tentativas = 0
let min = 1, max = 100

function jogarNovamente() {
  tentativas = 0
  sortear()
  btnAdivinhar.style.display = 'inline-block'
  resultado.innerHTML = `<p>Já pensei em um valor entre <strong>1</strong> e <strong>100</strong>...</p>`

  console.log(sorteio)
  console.log(tentativas)
}

function sortear() {  
  sorteio = Math.trunc(Math.random() * (max - min) + min)
}

function adivinhar() {
  palpite = Number(window.prompt('Qual é o seu palpite?').replace(',','.'))

  if (palpite % 1 != 0 && !isNaN(palpite % 1)) {
    resultado.innerHTML += `<p>Por favor, digite um número <strong>inteiro</strong>.</p>`
  }
  else {
    if (palpite >= min && palpite <= max) {
      tentativas++
      if (palpite > sorteio) {
        resultado.innerHTML += `<p>Você falou <strong>${palpite}</strong>. Meu número é <span>menor</span>!</p>`
      }
      else if (palpite < sorteio) {
        resultado.innerHTML += `<p>Você falou <strong>${palpite}</strong>. Meu número é <span>MAIOR</span>!</p>`
      }
      else {
        resultado.innerHTML += `<p><span>PARABÉNS</span>! Você acertou com <strong>${tentativas}</strong> tentativa(s)! Eu tinha sorteado o valor <mark>${sorteio}</mark>!</p>`
        btnAdivinhar.style.display = 'none'
      }
    }
    else {
      resultado.innerHTML += `<p>Por favor, digite um número entre ${min} e ${max}.</p>`
    } 
  }   
}
