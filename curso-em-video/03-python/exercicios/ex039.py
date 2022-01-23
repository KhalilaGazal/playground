# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou
# se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
genero = int(input('Digite o gênero (0 = masculino, 1 = feminino): '))

if genero == 1:
    print('Você não precisa se alistar.')
elif genero == 0:
    nascimento = int(input('Digite o ano de nascimento: '))
    atual = date.today().year

    idade = atual - nascimento
    tempo = abs(18 - idade)
    if idade < 18:
        ano = atual + tempo
        print(f'Seu alistamento será em {ano}.')
    elif idade == 18:
        print('É hora de se alistar.')
    else:
        ano = atual - tempo
        print(f'Seu alistamento foi em {ano}.')
else:
    print('Gênero precisa ser 0 ou 1!')
