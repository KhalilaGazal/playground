function converter() {
  let resultado = document.getElementById('resultado')
  let c = Number(prompt('Digite uma temperatura em °C (Celsius):'))

  let f = (c * 1.8 + 32).toLocaleString('pt-BR')
  let k = (c + 273.15).toLocaleString('pt-BR')

  resultado.innerHTML = `<h2>A temperatura de <span>${c.toLocaleString('pt-BR')}°C</span> corresponde a...</h2>`
  resultado.innerHTML += `<p><span>${k}K</span> (Kelvin)</p>`
  resultado.innerHTML += `<p><span>${f}°F</span> (Fahrenheit)</p>`
}
