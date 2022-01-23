"""inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for x in range(inicio, fim + 1, passo):
    print(x)"""

soma = 0
for x in range(0, 4):
    numero = int(input('Digite um valor: '))
    soma += numero
print(f'O somatório de todos os números foi {soma}')
