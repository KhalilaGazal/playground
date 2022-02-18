function contar() {
  let resultado = window.document.getElementById('resultado')  
  let numero = Number(window.document.getElementById('numero').value)

  let hand = String.fromCodePoint(0x1F449)
  let flag = String.fromCodePoint(0x1F3C1)

  resultado.innerHTML += `<h2>Contando de 0 até ${numero}</h2>`

  for (let i = 0; i <= numero; i++) {
    resultado.innerHTML += ` ${i} ${hand} `   
  }  
  resultado.innerHTML += `${flag}`
}