# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

pessoa = dict()
currentYear = datetime.now().year

pessoa['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
pessoa['idade'] = currentYear - nascimento
pessoa['ctps'] = int(input('Carteira de trabalho (0 = não possui): '))

if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$'))

    pessoa['aposentadoria'] = pessoa['contratacao'] + 35 - nascimento

for k, v in pessoa.items():
    print(f'{k}: {v}')
