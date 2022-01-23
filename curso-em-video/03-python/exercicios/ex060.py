# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

'''
from math import factorial
numero = int(input('Digite um número: '))
fatorial = factorial(numero)
print(f'{numero}! = {fatorial}')
'''

'''
numero = int(input('Digite um número: '))
count = numero
fatorial = 1
print(f'{numero}! = ', end='')
while count != 0:
    print(count, end='')
    print(' x ' if count != 1 else ' = ', end='')
    fatorial *= count
    count -= 1
print(f'{fatorial}')
'''

fatorial = 1

numero = int(input('Digite um número: '))

print(f'{numero}! = ', end='')

for x in range(numero, 0, -1):
    print(x, end='')
    print(' x ' if x != 1 else ' = ', end='')
    fatorial *= x

print(f'{fatorial}')
