function analisar() {
  let resultado = window.document.getElementById('resultado')
  let data = new Date

  let dia = data.getDate()
  let mes = data.getMonth()
  let ano = data.getFullYear()
  let semana = data.getDay()
  let hora = data.getHours()
  let minutos = data.getMinutes()
  let segundos = data.getSeconds()

  let meses = new Array('Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez')
  let diasSemana = new Array ('Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb')

  resultado.innerHTML = `<p>Dia: <mark>${dia}</mark></p>`
  resultado.innerHTML += `<p>Mês: <mark>${meses[mes]}</mark></p>`
  resultado.innerHTML += `<p>Ano: <mark>${ano}</mark></p>`
  resultado.innerHTML += `<p>Dia da semana: <mark>${diasSemana[semana]}</mark></p>`
  resultado.innerHTML += `<p>Hora: <mark>${hora}</mark></p>`
  resultado.innerHTML += `<p>Minutos: <mark>${minutos}</mark></p>`
  resultado.innerHTML += `<p>Segundos: <mark>${segundos}</mark></p>`
}