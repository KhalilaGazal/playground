function iniciar() {
  let nome = ''
  let idade = -1
  while (nome.length == 0) {
    nome = prompt('Qual é o seu nome?')
  }
  while (idade < 0) {
    idade = prompt(`Olá, ${nome}! Quantos anos você tem?`)
  }
  alert(`Acabei de te conhecer, ${nome}, que tem ${idade} anos de idade!`)
}
