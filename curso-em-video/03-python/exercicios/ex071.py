# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e
# o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

saque = int(input('Digite o valor a ser sacado: R$'))
resto = saque

cedula50 = saque // 50
resto %= 50
cedula20 = resto // 20
resto %= 20
cedula10 = resto // 10
resto %= 10
cedula1 = resto

if cedula50 > 0:
    print(f'Cédulas de R$50 = {cedula50}')
if cedula20 > 0:
    print(f'Cédulas de R$20 = {cedula20}')
if cedula10 > 0:
    print(f'Cédulas de R$10 = {cedula10}')
if cedula1 > 0:
    print(f'Cédulas de R$1 = {cedula1}')

'''
saque = int(input('Digite o valor a ser sacado: R$'))

cedula = 50
totalCedula = 0
total = saque

while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'Cédulas de R${cedula} = {totalCedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0

        if total == 0:
            break
'''
