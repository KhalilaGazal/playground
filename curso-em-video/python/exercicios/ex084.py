# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista = []
temp = []
maior = menor = 0

while True:
    flag = ' '

    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(lista) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]

    lista.append(temp[:])
    temp.clear()

    while flag not in 'sn':
        flag = str(input('Quer continuar? [S/N] ')).lower()
    if flag == 'n':
        break

print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'Pessoa(s) mais pesada(s): ', end='')
for pessoa in lista:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}] ', end='')
print()
print(f'Pessoa(s) mais leve(s): ', end='')
for pessoa in lista:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}] ', end='')
