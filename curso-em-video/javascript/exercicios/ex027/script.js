function calcular() {
  let resultado = window.document.getElementById('resultado')  
  let numero = Number(window.document.getElementById('numero').value)
  let mult

  resultado.innerHTML = `<h2>Tabuada de ${numero}</h2>`

  for (let i = 1; i <= 10; i++) {
    mult = numero * i
    resultado.innerHTML += `${numero} x ${i} = <strong>${mult}</strong><br>`
  }
}
