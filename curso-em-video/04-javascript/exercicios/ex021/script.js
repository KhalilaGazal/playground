function contar() {
  let resultado = window.document.getElementById('resultado')  

  let hand = String.fromCodePoint(0x1F449)
  let flag = String.fromCodePoint(0x1F3C1)

  resultado.innerHTML += `<h2>Contando de 1 até 10</h2>`

  for (let i = 1; i <= 10; i++) {
    resultado.innerHTML += `${i} ${hand} `
  }
  
  resultado.innerHTML += `${flag}`
}