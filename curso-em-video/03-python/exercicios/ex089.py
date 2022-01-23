# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que
# o usuário possa mostrar as notas de cada aluno individualmente.

lista = list()

while True:
    flag = ' '

    nome = str(input('Digite o nome: '))
    nota1 = float(input('Digite a 1ª nota: '))
    nota2 = float(input('Digite a 2ª nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])

    while flag not in 'sn':
        flag = str(input('Quer continuar? [S/N] ')).lower()
    if flag == 'n':
        break

print()
print(f'{"Nº":<6}{"NOME":<20}{"MÉDIA":>10}')
print('-' * 40)

for i, aluno in enumerate(lista):
    print(f'{i:<6}{aluno[0]:<20}{aluno[2]:>10.1f}')

flag2 = 999
while True:
    numero = int(input(f'\nDigite o nº de um aluno para mostrar suas notas ou {flag2} para sair: '))

    if numero == flag2:
        break

    if numero <= len(lista) - 1:
        print(f'\n{"NOME":<20}{"NOTAS":>10}')
        print('-' * 35)
        print(f'{lista[numero][0]:<20}{lista[numero][1]}')
