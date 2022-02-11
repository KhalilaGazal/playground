function verificar() {
  var anoNasc = window.document.getElementById('ano-nasc').value
  var genero = window.document.getElementsByName('genero')
  var resultado = window.document.getElementById('resultado') 

  var data = new Date()
  var anoAtual = data.getFullYear()

  var imagem = document.createElement('img')
  imagem.setAttribute('id', 'foto')

  var homem = genero[0].checked
  if (genero[0].checked) {
    genero = 'homem'
  }
  else {
    genero = 'mulher'
  }

  if (anoNasc.length == 0 || anoAtual < anoNasc || anoNasc < 1900) {
    window.alert('[ERRO] Verifique os dados e tente novamente!')
  }
  else {
    var idade = anoAtual - anoNasc
    var crianca = 10
    var jovem = 21
    var adulto = 50

    if (idade < crianca) {
      imagem.setAttribute('src', `./img/crianca-${genero}.png`)
    }
    else if (idade < jovem) {
      imagem.setAttribute('src', `./img/jovem-${genero}.png`)
    }
    else if (idade < adulto) {
      imagem.setAttribute('src', `./img/adulto-${genero}.png`)
    }
    else
    {
      imagem.setAttribute('src', `./img/idoso-${genero}.png`)
    }

    /*
    if (idade < crianca) {
      if (homem) {
        imagem.setAttribute('src', './img/crianca-homem.png')
      }
      else {
        imagem.setAttribute('src', './img/crianca-mulher.png')
      }
    }
    else if (idade < jovem) {
      if (homem) {
        imagem.setAttribute('src', './img/jovem-homem.png')
      }
      else {
        imagem.setAttribute('src', './img/jovem-mulher.png')
      }
    }
    else if (idade < adulto) {
      if (homem) {
        imagem.setAttribute('src', './img/adulto-homem.png')
      }
      else {
        imagem.setAttribute('src', './img/adulto-mulher.png')
      }
    }
    else {
      if (homem) {
        imagem.setAttribute('src', './img/idoso-homem.png')
      }
      else {
        imagem.setAttribute('src', './img/idoso-mulher.png')
      }
    }
    */

    resultado.style.textAlign = 'center'
    resultado.innerHTML = `<p>Detectamos ${genero} de ${idade} anos.</p>`
    resultado.appendChild(imagem)
  } 
}