# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input('Digite o 1º termo: '))
razao = int(input('Digite a razão: '))

count = 1

while count <= 10:
    print(termo, end='')
    print(' - ' if count != 10 else '', end='')
    termo += razao
    count += 1
