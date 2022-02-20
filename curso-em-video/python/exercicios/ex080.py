# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []

for i in range(0, 5):
    numero = int(input(f'Digite o {i+1}º número: '))
    if i == 0 or numero > lista[-1]:
        lista.append(numero)
        print(f'{numero} adicionado na última posição.')
    else:
        i = 0
        while i < len(lista):
            if numero <= lista[i]:
                lista.insert(i, numero)
                print(f'{numero} adicionado na {i+1}ª posição.')
                break
            i += 1

print(f'Lista ordenada: {lista}')
