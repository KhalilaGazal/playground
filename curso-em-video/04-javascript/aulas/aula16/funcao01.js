/*
* FUNÇÕES
- ações executadas assim que chamadas ou em decorrência de algum evento
- pode receber parâmetros e retornar um resultado
*/

function parImpar(n) {
  if (n % 2 == 0) {
    return 'Par!'
  }
  else {
    return 'Ímpar!'
  }
}

// let resultado = parImpar(4)
// console.log(resultado)

console.log(parImpar(4))