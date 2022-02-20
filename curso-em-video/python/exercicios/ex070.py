# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

menorPreco = preco = qtd = qtdMil = total = 0
menorNome = nome = ' '

while True:
    flag = ' '

    nome = str(input('Digite o nome do produto: '))
    preco = float(input(f'Digite o preço de "{nome}": R$'))

    total += preco
    qtd += 1

    if preco > 1000:
        qtdMil += 1
    if qtd == 1 or preco < menorPreco:
        menorPreco = preco
        menorNome = nome

    while flag not in 'SN':
        flag = str(input('Deseja continuar? [S/N] ')).upper()
    if flag == 'N':
        break

print(f'Total = R${total:.2f}')
print(f'Quantidade de produtos que custam mais de R$1000 = {qtdMil}')
print(f'Produto mais barato: {menorNome} (R${menorPreco:.2f})')
