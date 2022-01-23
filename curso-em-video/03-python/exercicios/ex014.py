# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Digite a temperatura em ºC: '))

fahrenheit = celsius * 1.8 + 32

print(f'{celsius:.1f}ºC = {fahrenheit:.1f}ºF')
