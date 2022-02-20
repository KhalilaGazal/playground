function contar() {
  let resultado = window.document.getElementById('resultado')  
  let inicio = Number(window.document.getElementById('inicio').value)
  let fim = Number(window.document.getElementById('fim').value)

  let hand = String.fromCodePoint(0x1F449)
  let flag = String.fromCodePoint(0x1F3C1)

  resultado.innerHTML = `<h2>Contando de ${inicio} até ${fim}</h2>`

  if (inicio < fim) {
    for (let i = inicio; i <= fim; i++) {
      resultado.innerHTML += ` ${i} ${hand} `   
    }  
  }
  else if (inicio > fim) {
    for (let i = inicio; i >= fim ; i--) {
      resultado.innerHTML += ` ${i} ${hand} `   
    }
  }
  else {
    resultado.innerHTML += 'Não é possível contar, pois os números são iguais '
  }

  resultado.innerHTML += `${flag}`
}
