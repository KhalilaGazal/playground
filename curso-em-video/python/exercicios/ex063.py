# Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

anterior = 1
fibonacci = 0

termos = int(input('Digite a quantidade de termos: '))

while termos > 0:
    print(fibonacci, end='')
    fibonacci += anterior
    anterior = fibonacci - anterior
    print(' - ' if termos != 1 else '', end='')
    termos -= 1
