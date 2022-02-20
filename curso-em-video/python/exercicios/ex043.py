# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
# mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

abaixo = 18.5
ideal = 25
sobrepreso = 30
obesidade = 40

peso = float(input('Digite o seu peso (kg): '))
altura = float(input('Digite a sua altura (m): '))

imc = peso / (altura * altura)

if imc < abaixo:
    categoria = 'abaixo do peso'
elif imc <= ideal:
    categoria = 'peso ideal'
elif imc <= sobrepreso:
    categoria = 'sobrepreso'
elif imc <= obesidade:
    categoria = 'obesidade'
else:
    categoria = "obesidade mórbida"

print(f'IMC = {imc:.1f}')
print(f'Categoria: {categoria}')
