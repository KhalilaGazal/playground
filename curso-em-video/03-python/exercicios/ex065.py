# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

maior = menor = qtd = soma = 0
resposta = 's'

while resposta in 's':
    numero = int(input('Digite um número: '))
    soma += numero
    qtd += 1
    if qtd == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Deseja continuar? [S/N] ')).lower()

media = soma / qtd

print(f'Números digitados = {qtd}')
print(f'Média = {media}')
print(f'Maior = {maior}')
print(f'Menor = {menor}')
