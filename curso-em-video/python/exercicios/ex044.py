# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print(f'{" Lojas Guanabara ":=^40}')

preco = float(input('Digite o valor do produto: R$'))
print('''Formas de pagamento
[1] à vista dinheiro/cheque (10% de desconto)
[2] à vista no cartão (5% de desconto)
[3] 2x no cartão (preço normal)
[4] 3x ou mais no cartão (20% de juros)''')
pagamento = int(input('Escolha a forma de pagamento: '))

if pagamento == 1:
    total = preco - preco * .1
elif pagamento == 2:
    total = preco - preco * 0.05
elif pagamento == 3:
    total = preco
    parcela = total / 2
    print(f'2x de R${parcela:.2f}')
elif pagamento == 4:
    qtd = int(input('Digite a quantidade de parcelas: '))
    total = preco + preco * 0.2
    parcela = total / qtd
    print(f'{qtd}x de R${parcela:.2f}')
else:
    total = preco
    print('Opção inválida de pagamento!')
print(f'Valor total da compra = R${total:.2f}')
