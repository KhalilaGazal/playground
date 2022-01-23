# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero1 = int(input('Digite o 1º númmero: '))
numero2 = int(input('Digite o 2º númmero: '))
numero3 = int(input('Digite o 3º númmero: '))

menor = numero1
maior = numero1

if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero1 and numero3 > numero2:
    maior = numero3

print(f'MENOR número = {menor}')
print(f'MAIOR número = {maior}')
