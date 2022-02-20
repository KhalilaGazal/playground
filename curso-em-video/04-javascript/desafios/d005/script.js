function converter() {
  let resultado = document.getElementById('resultado')
  let m = Number(prompt('Digite uma medida em metros (m):'))

  let km = (m / 1000).toLocaleString('pt-BR')
  let hm = (m / 100).toLocaleString('pt-BR')
  let dam = (m / 10).toLocaleString('pt-BR')
  let dm = (m * 10).toLocaleString('pt-BR')
  let cm = (m * 100).toLocaleString('pt-BR')
  let mm = (m * 1000).toLocaleString('pt-BR')

  resultado.innerHTML = `<h2>A distância de <strong>${m.toLocaleString('pt-BR')}</strong> metros corresponde a...</h2>`
  resultado.innerHTML += `<p><span>${km}</span> quilômetro(s) <span>(km)</span></p>`
  resultado.innerHTML += `<p><span>${hm}</span> hectômetro(s) <span>(hm)</span></p>`
  resultado.innerHTML += `<p><span>${dam}</span> decâmetro(s) <span>(dam)</span></p>`
  resultado.innerHTML += `<p><span>${dm}</span> decímetro(s) <span>(dm)</span></p>`
  resultado.innerHTML += `<p><span>${cm}</span> centímetro(s) <span>(cm)</span></p>`
  resultado.innerHTML += `<p><span>${mm}</span> milímetro(s) <span>(mm)</span></p>`
}
