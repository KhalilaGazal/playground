# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

numero = randint(0, 5)

palpite = int(input('Digite um número entre 0 e 5: '))

print('Processando...')
sleep(1)

if 0 <= palpite <= 5:
    if palpite == numero:
        msg = 'Parabéns, você venceu!'
    else:
        msg = 'Que pena, você perdeu! Tente novamente.'
    print(f'O computador pensou em... {numero}\n{msg}')
else:
    print('Número não está entre 0 e 5!')
