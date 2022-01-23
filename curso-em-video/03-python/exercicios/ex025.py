# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite o nome: '))

nome = nome.lower()
silva = 'silva' in nome

print(f'Tem Silva? {silva}')
