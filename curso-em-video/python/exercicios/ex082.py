# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que
# vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
par = []
impar = []

while True:
    flag = ' '

    numero = int(input(f'Digite um número: '))
    lista.append(numero)

    while flag not in 'sn':
        flag = str(input('Quer continuar? [S/N] ')).lower()
    if flag == 'n':
        break

for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f'Valores = {lista}')
print(f'Valores PARES = {par}')
print(f'Valores ÍMPARES= {impar}')
