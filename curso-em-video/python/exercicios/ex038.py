# Escreva um programa que leia dois números inteiros e compare-os. Mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

if numero1 > numero2:
    print('O PRIMEIRO valor é maior.')
elif numero1 < numero2:
    print('O SEGUNDO valor é maior.')
else:
    print('Os dois valores são IGUAIS.')
