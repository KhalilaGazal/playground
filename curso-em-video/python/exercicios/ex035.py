# Desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo.

reta1 = float(input('Digite o comprimento da 1ª reta: '))
reta2 = float(input('Digite o comprimento da 2ª reta: '))
reta3 = float(input('Digite o comprimento da 3ª reta: '))

if abs(reta2 - reta3) < reta1 < (reta2 + reta3) and \
   abs(reta1 - reta3) < reta2 < (reta1 + reta3) and \
   abs(reta1 - reta2) < reta3 < (reta1 + reta2):
    print('Podem formar triângulo!')
else:
    print('NÃO podem formar triângulo!')
