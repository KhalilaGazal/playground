# Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

flag = 999
numero = soma = qtd = 0

while True:
    numero = int(input(f'Digite um número ou {flag} para parar: '))
    if numero == flag:
        break
    soma += numero
    qtd += 1

print(f'Quantidade de números digitados = {qtd}')
print(f'Soma = {soma}')
