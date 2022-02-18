function contar() {
  let resultado = window.document.getElementById('resultado')  

  let hand = String.fromCodePoint(0x1F449)
  let flag = String.fromCodePoint(0x1F3C1)

  resultado.innerHTML += `<h2>Contando de 1 até 10, marcando os pares</h2>`

  for (let i = 1; i <= 10; i++) {
    if (i % 2 == 0) {
      resultado.innerHTML += `<mark><strong> ${i} </strong></mark>${hand} `      
    }
    else {
      resultado.innerHTML += ` ${i} ${hand}`
    }
  }
  
  resultado.innerHTML += `${flag}`
}