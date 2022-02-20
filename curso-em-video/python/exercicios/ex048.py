# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e
# que se encontram no intervalo de 1 até 500.

soma = 0
qtd = 0

for x in range(1, 501, 2):
    if x % 3 == 0:
        soma += x
        qtd += 1

print(f'A soma dos {qtd} valores é {soma}.')
