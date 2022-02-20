# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

oposto = float(input("Digite o comprimento do cateto OPOSTO: "))
adjacente = float(input("Digite o comprimento do cateto ADJACENTE: "))
hipotenusa = (oposto ** 2 + adjacente ** 2) ** (1/2)
print(f'Hipotenusa = {hipotenusa:.2f}')

'''from math import hypot
oposto = float(input("Digite o comprimento do cateto OPOSTO: "))
adjacente = float(input("Digite o comprimento do cateto ADJACENTE: "))
hipotenusa = hypot(oposto, adjacente)
print(f'Hipotenusa = {hipotenusa:.2f}')'''
