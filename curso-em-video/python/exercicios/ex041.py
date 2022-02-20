# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
# mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date

ano = date.today().year
mirim = 9
infantil = 14
junior = 19
senior = 25

nascimento = int(input('Digite o ano de nascimento: '))

idade = ano - nascimento

if idade <= mirim:
    categoria = 'mirim'
elif idade <= infantil:
    categoria = 'infantil'
elif idade <= junior:
    categoria = 'júnior'
elif idade <= senior:
    categoria = 'sênior'
else:
    categoria = 'master'

print(f'Idade: {idade} anos')
print(f'Categoria: {categoria}')
