# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = dict()

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))

print()

if aluno['Média'] >= 7:
    aluno['Situação'] = 'aprovado'
elif aluno['Média'] >= 5:
    aluno['Situação'] = 'recuperação'
else:
    aluno['Situação'] = 'reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}.')
