# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

homem = mulher = maior = 0

while True:
    idade = -1
    flag = genero = ' '

    print('=' * 20)

    while idade < 0:
        idade = int(input('Digite a idade: '))

    while genero not in 'HMO':
        print('[H] Homem')
        print('[M] Mulher')
        print('[O] Outro')
        genero = str(input('Digite um gênero: ')).upper()

    while flag not in 'SN':
        flag = str(input('Quer continuar? [S/N] ')).upper()

    if idade > 18:
        maior += 1
    if genero == 'H':
        homem += 1
    if idade < 20 and genero == 'M':
        mulher += 1

    if flag == 'N':
        break

print(f'Pessoas maiores de 18 anos = {maior}')
print(f'Homens cadastrados = {homem}')
print(f'Mulheres com menos de 20 anos = {mulher}')
