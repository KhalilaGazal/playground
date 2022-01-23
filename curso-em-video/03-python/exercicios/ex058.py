# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora
# o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

numero = randint(0, 10)
palpite = -1
tentativa = 1

while palpite < 0 or palpite > 10:
    palpite = int(input('Digite um número entre 0 e 10: '))

while numero != palpite:
    while palpite < 0 or palpite > 10:
        palpite = int(input('Digite um número entre 0 e 10: '))
    if palpite > numero:
        palpite = int(input('Palpite errado! Tente um número menor: '))
    elif palpite < numero:
        palpite = int(input('Palpite errado! Tente um número maior: '))
    tentativa += 1

print(f'Parabéns, você acertou com {tentativa} tentativa(s)!')
