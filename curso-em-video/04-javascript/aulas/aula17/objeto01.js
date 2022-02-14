let test = [] // array = objeto
// console.log(typeof test) 

// let amigo = {nome: 'José', genero: 'M', peso: 85.4}
let amigo = {nome: 'José', 
genero: 'M', 
peso: 85.4,
engordar(p = 0) {
  console.log('Engordou')
  this.peso += p
}}

// console.log(typeof amigo)

// console.log(amigo)
// console.log(amigo.nome)

amigo.engordar(2)
console.log(`${amigo.nome} pesa ${amigo.peso}kg`)