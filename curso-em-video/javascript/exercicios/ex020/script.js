function iniciar() {
  let resultado = window.document.getElementById('resultado')
  
  let mes = window.prompt('Digite o mês por extenso (ex: Setembro):').toLowerCase()
  let estacao

  switch (mes) {
    case 'janeiro': case 'fevereiro': case 'março':
      estacao = 'verão'
      break
    case 'abril': case 'maio': case 'junho':
      estacao = 'outono'
      break
    case 'julho': case 'agosto': case 'setembro':
      estacao = 'inverno'
      break
    case 'outubro': case 'novembro': case 'dezembro':
      estacao = 'primavera'
      break
    default:
      estacao = 'indefinida'
      break
  }

  resultado.innerHTML = `<p>No mês de <strong>${mes.toUpperCase()}</strong>, estamos na estação <mark><strong>${estacao.toUpperCase()}</strong></mark>!</p>`
}
