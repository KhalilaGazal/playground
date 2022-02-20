# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
posicaoMaior = []
posicaoMenor = []

for i in range(0, 5):
    lista.append(input(f'Digite o {i+1}º número: '))

maior = max(lista)
menor = min(lista)
for i, numeros in enumerate(lista):
    if numeros == maior:
        posicaoMaior.append(i)
    if numeros == menor:
        posicaoMenor.append(i)

print(f'Lista: {lista}')
print(f'Maior número: {maior} nas posições {posicaoMaior}')
print(f'Menor número: {menor} nas posições {posicaoMenor}')
