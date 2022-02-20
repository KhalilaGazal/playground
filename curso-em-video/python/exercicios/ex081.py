# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = list()

while True:
    flag = ' '

    numero = int(input(f'Digite um número: '))
    if numero in lista:
        print('Valor NÃO será adicionado porque já está na lista.')
    else:
        lista.append(numero)
        print('Valor adicionado!')

    while flag not in 'sn':
        flag = str(input('Quer continuar? [S/N] ')).lower()
    if flag == 'n':
        break

qtd = len(lista)
lista.sort(reverse=True)
if 5 in lista:
    cinco = 'ESTÁ'
else:
    cinco = 'NÃO está'

print(f'Quantidade de números digitados = {qtd}')
print(f'Valores em ordem DECRESCENTE = {lista}')
print(f'O valor 5 {cinco} na lista.')
