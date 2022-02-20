function calcular() {
  let resultado = window.document.getElementById('resultado')
  
  let numero1 = Number(window.prompt('Primeiro valor:').replace(',','.'))
  let numero2 = Number(window.prompt('Segundo valor:').replace(',','.'))
  let opcao = Number(window.prompt(`Valores informados: ${numero1} e ${numero2}. \nO que vamos fazer?\n[1] Somar\n[2] Subtrair\n[3] Multiplicar\n[4] Dividir`))
  
  let calculo = 0
  let mensagem
  
  switch (opcao) {
    case 1:
      calculo = numero1 + numero2
      mensagem = `<strong>${numero1.toLocaleString('pt-BR')}</strong> + <strong>${numero2.toLocaleString('pt-BR')}</strong> = <span>${calculo.toLocaleString('pt-BR')}</span>`
      break
    case 2:
      calculo = numero1 - numero2
      mensagem = `<strong>${numero1.toLocaleString('pt-BR')}</strong> - <strong>${numero2.toLocaleString('pt-BR')}</strong> = <span>${calculo.toLocaleString('pt-BR')}</span>`
      break
    case 3:
      calculo = numero1 * numero2
      mensagem = `<strong>${numero1.toLocaleString('pt-BR')}</strong> x <strong>${numero2.toLocaleString('pt-BR')}</strong> = <span>${calculo.toLocaleString('pt-BR')}</span>`
      break
    case 4:
      calculo = numero1 / numero2
      mensagem = `<strong>${numero1.toLocaleString('pt-BR')}</strong> / <strong>${numero2.toLocaleString('pt-BR')}</strong> = <span>${calculo.toLocaleString('pt-BR')}</span>`
      break
    default:
      mensagem = `OPÇÃO INVÁLIDA! Você digitou <strong>${numero1.toLocaleString('pt-BR')}</strong> e <strong>${numero2.toLocaleString('pt-BR')}</strong> mas não sei o que fazer com eles. `
      break
  }

  resultado.innerHTML = `<h2>Calculando...</h2><p>${mensagem}</p>`
}
