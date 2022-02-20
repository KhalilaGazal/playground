# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = soma = maior = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um número [{linha}, {coluna}]: '))

        if matriz[linha][coluna] % 2 == 0:
            par += matriz[linha][coluna]

        if coluna == 0 or matriz[1][coluna] > maior:
            maior = matriz[1][coluna]

    soma += matriz[linha][2]

print(f'Soma dos valores pares = {par}')
print(f'Soma dos valores da terceira coluna = {soma}')
print(f'Maior valor da segunda linha = {maior}')
