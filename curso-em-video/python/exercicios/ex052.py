# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

primo = True
numero = int(input('Digite um número inteiro: '))

if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
else:
    primo = False
if primo:
    print(f'{numero} é um número primo!')
else:
    print(f'{numero} NÃO é um número primo!')
