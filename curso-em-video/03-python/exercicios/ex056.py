# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e
# quantas mulheres têm menos de 20 anos.

erro = False
nome = {}
idade = {}
genero = {}
pessoas = 4
soma = 0
mulheres = 0

for i in range(0, pessoas):
    print('\n' + ('=' * 10) + f' PESSOA {i + 1} ' + ('=' * 10))
    nome[i] = str(input(f'Digite o nome da {i + 1}ª pessoa: '))
    idade[i] = int(input(f'Digite a idade da {i + 1}ª pessoa: '))
    print('[H] Homem | [M] Mulher | [O] Outro')
    genero[i] = str(input(f'Digite o gênero da {i + 1}ª pessoa: ')).lower()
    if not (genero[i] == 'h' or genero[i] == 'm' or genero[i] == 'o'):
        erro = True
        break

maior = idade[0]

if erro:
    print('[ERRO] Gênero deve ser "H", "M" ou "O"')
else:
    for i in range(0, pessoas):
        soma += idade[i]
        if genero[i] == 'h':
            if idade[i] > maior:
                maior = idade[i]
                nome = nome[i]
        if genero[i] == 'm':
            if idade[i] < 20:
                mulheres += 1
    media = soma / pessoas
    print(f'\nMédia: {media} anos')
    print(f'Homem mais velho: {nome}')
    print(f'Mulheres com menos de 20 anos: {mulheres}')
