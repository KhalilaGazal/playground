# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pessoas = 5
peso = {}

for i in range(0, pessoas):
    peso[i] = float(input(f'Digite o peso da {i + 1}ª pessoa: '))
maior = peso[0]
menor = peso[0]

for i in range(0, pessoas):
    if peso[i] > maior:
        maior = peso[i]
    if peso[i] < menor:
        menor = peso[i]

print(f'Maior peso = {maior}kg\nMenor peso = {menor}kg')
