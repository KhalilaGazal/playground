# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

ano = date.today().year
maior = 0
pessoas = 7

for i in range(0, pessoas):
    nascimento = int(input(f'Digite o ano de nascimento da {i + 1}ª pessoa: '))
    if ano - nascimento >= 21:
        maior += 1

menor = pessoas - maior

print(f'Maior de idade: {maior} pessoa(s)\nMenor de idade: {menor} pessoa(s)')


