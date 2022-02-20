# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

flag = 999
numero = qtd = soma = 0

numero = int(input(f'Digite um número ou {flag} para parar: '))

while numero != flag:
    soma += numero
    qtd += 1
    numero = int(input(f'Digite um número ou {flag} para parar: '))

print(f'Você digitou {qtd} número(s) e a soma é igual a {soma}.')
