# Faça um programa que leia algo pelo teclado e
# mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

txt = input('Digite algo: ')

numeric = txt.isnumeric()
alpha = txt.isalpha()
alphanumeric = txt.isalnum()
upper = txt.isupper()
lower = txt.islower()
title = txt.istitle()
space = txt.isspace()
type = type(txt)

print(f'"{txt}" é do tipo primitivo {type}')
print(f'É numérico? {numeric}')
print(f'É alfabético? {alpha}')
print(f'É alfanumérico? {alphanumeric}')
print(f'Está somente em letras maiúsculas? {upper}')
print(f'Está somente em letras minúsculas? {lower}')
print(f'Está capitalizada? {title}')
print(f'Só tem espaços? {space}')
