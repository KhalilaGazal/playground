function carregar() {
  var data = new Date()
  var hora = data.getHours()
  var msg = window.document.getElementById('msg')
  var imagem = window.document.getElementById('imagem')

  msg.innerHTML = `<p>Agora são <strong>${hora}</strong> hora(s)</p>`

  if (hora < 6) {
    imagem.src = './img/madrugada.jpg'
    msg.innerHTML += '<p>Boa madrugada!</p>'
    document.body.style.background = '#7a3b4c'
  }
  else if (hora < 12) {
    imagem.src = './img/manha.jpg'
    msg.innerHTML += '<p>Bom dia!</p>'
    document.body.style.background = '#ffca6d'
  }
  else if (hora < 18) {
    imagem.src = './img/tarde.jpg'
    msg.innerHTML += '<p>Boa tarde!</p>'
    document.body.style.background = '#fe7330'
  }
  else {
    imagem.src = './img/noite.jpg'
    msg.innerHTML += '<p>Boa noite!</p>'
    document.body.style.background = '#1b1f2b'
  }
}