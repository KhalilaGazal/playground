# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import sample

sorteio = tuple(sample(range(1, 10), 5))
menor = min(sorteio)
maior = max(sorteio)

print(f'Números sorteados = {sorteio}')
print(f'Menor número = {menor}')
print(f'Maior número = {maior}')
