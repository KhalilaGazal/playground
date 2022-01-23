# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# Ex: Digite um número: 6.127. O número 6.127 tem a parte Inteira 6.

numero = float(input('Digite um valor: '))
inteiro = int(numero)
print(f'Porção inteira = {inteiro}')

'''from math import trunc
numero = float(input('Digite um valor: '))
inteiro = trunc(numero)
print(f'Porção inteira = {inteiro}')'''
