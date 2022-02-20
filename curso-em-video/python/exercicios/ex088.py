# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e
# vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import sample

lista = []
jogos = int(input('Quantos jogos? '))

for i in range(0, jogos):
    sorteio = sample(range(1, 61), 6)
    sorteio.sort()
    lista.append(sorteio)
    print(f'{i+1}º = {lista[i]}')
