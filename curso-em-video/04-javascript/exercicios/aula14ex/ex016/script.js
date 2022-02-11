function contar() {
  let inicio = Number(document.getElementById('inicio').value)
  let fim = Number(document.getElementById('fim').value)
  let passo = Number(document.getElementById('passo').value)
  let resultado = document.getElementById('resultado')

  let hand = String.fromCodePoint(0x1F449)
  let flag = String.fromCodePoint(0x1F3C1)

  if (inicio == '' || fim == '') {
    resultado.innerHTML = '<p>Impossível contar!</p>'
  }
  else {
    if (passo == '') {
      passo = 1
      alert('Passo inválido! Considerando PASSO 1.')
    }
    
    resultado.innerHTML = '<p>Contando:</p>' 

    if (inicio <= fim) {
      for (let i = inicio; i <= fim; i += passo) {
        resultado.innerHTML += ` ${i} ${hand}`
      }
    }
    else {
      for (let i = inicio; i >= fim; i -= passo) {
        resultado.innerHTML += ` ${i} ${hand}`
      }
    }

    resultado.innerHTML += flag
  }
}