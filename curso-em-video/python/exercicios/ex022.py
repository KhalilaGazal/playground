# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()

maiusculo = nome.upper()
minusculo = nome.lower()
qtd = len(nome.replace(" ", ""))
split = nome.split()
primeiro = split[0]
qtd_primeiro = len(split[0])

print(f'Nome em MAIÚSCULAS = {maiusculo}')
print(f'Nome em MINÚSCULAS = {minusculo}')
print(f'Nome COMPLETO = {qtd} letras')
print(f'PRIMEIRO nome = {qtd_primeiro} letras')
