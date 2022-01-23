# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

jogadorEscolha = ' '
vitoria = 0
impar = 'ÍMPAR'
par = 'PAR'

while True:
    computadorNumero = randint(0, 10)

    while jogadorEscolha not in 'IP':
        jogadorEscolha = str(input('Par ou ímpar? [P/I] ')).upper()
    jogadorNumero = -1
    while jogadorNumero < 0 or jogadorNumero > 10:
        jogadorNumero = int(input('Escolha um número entre 0 e 10: '))
    if jogadorEscolha == 'I':
        jogadorEscolha = impar
    else:
        jogadorEscolha = par

    soma = computadorNumero + jogadorNumero
    if soma % 2 == 0:
        partida = par
    else:
        partida = impar

    if jogadorEscolha == partida:
        resultado = 'GANHOU'
        vitoria += 1
    else:
        resultado = 'PERDEU'

    print(f'VOCÊ jogou {jogadorNumero}')
    print(f'COMPUTADOR jogou {computadorNumero}')
    print(f'Total = {soma} = {partida}')
    print('=' * 20)
    print(f'Você {resultado}!')
    print('=' * 20)

    if jogadorEscolha != partida:
        print(f'GAME OVER!\nTotal de vitórias = {vitoria}')
        break
