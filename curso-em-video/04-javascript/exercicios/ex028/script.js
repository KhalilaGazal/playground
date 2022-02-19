function calcular() {
  let resultado = window.document.getElementById('resultado')  
  let numero = Number(window.document.getElementById('numero').value)
  let fatorial = 1

  resultado.innerHTML += `<h2>Calculando <span>${numero}!</span></h2>`

  for (let i = numero; i >= 1; i--) {
    fatorial *= i

    resultado.innerHTML += `${i}`
    if (i != 1) {
      resultado.innerHTML += ` x `
    }
  }

  resultado.innerHTML += ` = <strong>${fatorial.toLocaleString('pt-BR')}</strong>`
}
