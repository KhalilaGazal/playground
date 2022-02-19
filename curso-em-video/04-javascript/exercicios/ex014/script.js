function iniciar() {
  let resultado = window.document.getElementById('resultado')
  let data = new Date()

  resultado.innerHTML = `<p>O que eu recebi do sistema foi <mark>${data}</mark></p>`
}
