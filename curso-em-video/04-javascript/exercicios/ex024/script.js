function contar() {
  let resultado = window.document.getElementById('resultado')  

  let hand = String.fromCodePoint(0x1F449)
  let flag = String.fromCodePoint(0x1F3C1)

  resultado.innerHTML += `<h2>Contagem Regressiva de 10 a 1</h2>`

  for (let i = 10; i >= 1; i--) {
    resultado.innerHTML += ` ${i} ${hand} `   
  }
  
  resultado.innerHTML += `${flag}`
}