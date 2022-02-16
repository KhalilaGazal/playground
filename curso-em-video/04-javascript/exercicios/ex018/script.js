let resultado = window.document.getElementById('resultado')
let sorteio = 0, palpite = 0

function sortear() {
  let min = 1
  let max = 100
  sorteio = Math.trunc(Math.random() * (max - min) + min)
}

function adivinhar() {
  palpite = window.prompt('Qual é o seu palpite?')

  if (palpite > sorteio) {
    resultado.innerHTML += `<p>Você falou ${palpite}. Meu número é <strong>MENOR!</strong></p>`
  }
  else if (palpite < sorteio) {
    resultado.innerHTML += `<p>Você falou ${palpite}. Meu número é <strong>MAIOR!</strong></p>`

  }
  else {
    resultado.innerHTML += `<p><strong>PARABÉNS!</strong> Você acertou! Eu tinha sorteado o valor ${sorteio}!</p>`
    document.getElementById('btn').style.visibility = 'hidden'
  }
}