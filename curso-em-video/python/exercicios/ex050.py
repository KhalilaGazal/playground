# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

numero = 0
soma = 0
qtd = 6

for x in range(1, qtd + 1):
    numero = int(input(f'Digite o {x}º número: '))
    if numero % 2 == 0:
        soma += numero

print(f'Soma = {soma}')
