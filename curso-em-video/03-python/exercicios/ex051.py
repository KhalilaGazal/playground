#  Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#  No final, mostre os 10 primeiros termos dessa progressão.

'''pa = 0
termo = int(input('Digite o 1º termo: '))
razao = int(input('Digite a razão: '))
for x in range(1, 11):
    pa = termo + (x - 1) * razao
    print(f'{pa} ', end='')'''

termo = int(input('Digite o 1º termo: '))
razao = int(input('Digite a razão: '))

decimo = termo + 9 * razao

for i in range(termo, decimo + razao, razao):
    print(f'{i} ', end='')
