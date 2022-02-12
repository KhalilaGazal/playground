let vetor = [5, 8, 2, 9, 3]

console.log(`Nosso vetor é o ${vetor}`)

console.log(`\nO vetor tem ${vetor.length} posições.`)

console.log(`\nVetor na posição 0 = ${vetor[0]}`)

vetor.push(1)
console.log(`\nAdicionar número no final do vetor = ${vetor}`)

console.log(`\nOrdenar vetor = ${vetor.sort()}`)

console.log()

for (let pos = 0; pos < vetor.length; pos++) {
  console.log(`A posição ${pos} do vetor tem valor ${vetor[pos]}`)
}

console.log()

for (let pos in vetor) {
  console.log(`A posição ${pos} do vetor tem valor ${vetor[pos]}`)
}

console.log(`\nO valor 9 está na posição ${vetor.indexOf(9)}`)

console.log(`\nCaso o valor não seja encontrado = ${vetor.indexOf(99)}`)


let valor = 105
let posicao = vetor.indexOf(valor)

if (posicao == -1) {
  console.log(`\nO valor ${valor} não foi encontrado!`)
}
else {
  console.log(`\nO valor ${valor} foi encontrado na posição ${posicao}!`)
}