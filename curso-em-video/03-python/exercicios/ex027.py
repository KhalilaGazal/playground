# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e
# o último nome separadamente. Ex: Ana Maria de Souza (primeiro = Ana; último = Souza).

nome = str(input('Digite o nome completo: '))

nome = nome.split()
primeiro = nome[0]
ultimo = nome[-1]

print(f'Primeiro nome: {primeiro}')
print(f'Último nome: {ultimo}')
