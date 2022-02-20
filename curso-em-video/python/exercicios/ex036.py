# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Digite o valor do imóvel: R$'))
salario = float(input('Digite o valor do salário do comprador: R$'))
anos = int(input('Digite a quantidade de anos em que o imóvel será pago: '))

prestacao = valor / (anos * 12)
excedente = .3 * salario

if prestacao >= excedente:
    msg = 'Empréstimo NEGADO!'
else:
    msg = 'Empréstimo APROVADO!'

print(f'Prestação = R${prestacao:.2f}')
print(msg)
