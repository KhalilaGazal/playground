# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

lista = tuple(int(input(f'Digite o {i+1}º número: ')) for i in range(0, 4))
nove = lista.count(9)
if 3 in lista:
    tres = lista.index(3) + 1
pares = [i for i in lista if i % 2 == 0]

print(f'Números digitados: {lista}')
print(f'O número nove aparece {nove} vez(es).')
if 3 in lista:
    print(f'O primeiro valor três aparece na {tres}ª posição.')
else:
    print('O valor três não foi digitado em nenhuma posição.')
print(f'Números pares = {pares}')
