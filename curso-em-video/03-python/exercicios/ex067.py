# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    numero = int(input('\nDigite um número para ver sua tabuada (digite um número negativo para parar): '))
    if numero < 0:
        break
    print('=' * 15)
    print(f'Tabuada do {numero}')
    print('=' * 15)
    for i in range(1, 11):
        tabuada = i * numero
        print(f'{numero} x {i:2} = {tabuada}')
