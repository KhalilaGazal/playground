function calcular() {
  let n = document.getElementById('numero')
  let resultado = document.getElementById('resultado')  

  if (n.value.length == 0) {
    alert('Por favor, digite um número!')
  }
  else {
    let numero = Number(n.value)
    resultado.innerHTML = ''

    for (let i = 1; i <= 10; i++) {
      let item = document.createElement('option')
      item.value = `item${i}`
      item.text = `${numero} x ${i} = ${numero * i}`
      resultado.appendChild(item)
    }
  }  
}