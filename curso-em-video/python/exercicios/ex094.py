# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoa = dict()
dados = list()
idade = soma = 0

while True:
    flag = ' '

    pessoa['nome'] = str(input('\nNome: '))
    pessoa['genero'] = ' '
    while pessoa['genero'] not in 'hmo':
        pessoa['genero'] = str(input('Gênero (H = homem, M = mulher, O = outro): [H/M/O] ')).lower()
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    dados.append(pessoa.copy())

    while flag not in 'sn':
        flag = str(input('Quer continuar? [S/N] ')) .lower()
    if flag == 'n':
        break

qtd = len(dados)
media = soma / qtd

print(f'\nForam cadastradas {qtd} pessoa(s).')

print(f'A média das idades é igual a {media} anos.')

print('Mulheres cadastradas:')
for pessoa in dados:
    if pessoa['genero'] in 'm':
        print(f'- {pessoa["nome"]}')

print('Idade acima da média:')
for pessoa in dados:
    if pessoa['idade'] > media:
        print('- ', end='')
        for k, v in pessoa.items():
            print(f'{k}: {v} | ', end='')
        print()
