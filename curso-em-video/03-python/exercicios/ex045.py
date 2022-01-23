# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

opcao = ('PEDRA', 'PAPEL', 'TESOURA')

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Escolha uma opção: '))

if jogador != 0 and jogador != 1 and jogador != 2:
    print('Jogada inválida! Tente novamente!')
else:
    computador = randint(0, 2)
    pedra = 0
    papel = 1
    tesoura = 2

    print('JO')
    sleep(.5)
    print('KEN')
    sleep(.5)
    print('PÔ!')

    print('=' * 20)
    print(f'Jogador jogou {opcao[jogador]}')
    print(f'Computador jogou {opcao[computador]}')
    print('=' * 20)

    if jogador == computador:
        vencedor = 'EMPATE'
    elif jogador == pedra:
        if computador == papel:
            vencedor = 'COMPUTADOR'
        else:
            vencedor = 'JOGADOR'
    elif jogador == papel:
        if computador == pedra:
            vencedor = 'JOGADOR'
        else:
            vencedor = 'COMPUTADOR'
    else:
        if computador == pedra:
            vencedor = 'COMPUTADOR'
        else:
            vencedor = 'JOGADOR'
    print(f'Vencedor: {vencedor}')
