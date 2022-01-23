# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

colocacao = 'Atlético-MG', 'Palmeiras', 'Bragantino', 'Fortaleza', 'Flamengo', 'Internacional', 'Corinthians', \
            'Fluminense', 'Atlético-GO', 'América-MG', 'Cuiabá', 'Athletico-PR', 'São Paulo', 'Ceará', 'Bahia', \
            'Santos', 'Juventude', 'Sport', 'Grêmio', 'Chapecoense'

primeiros = colocacao[0:5]
ultimos = colocacao[-4:]
alfabetica = sorted(colocacao)
chapecoense = colocacao.index('Chapecoense') + 1

print(f'Lista de times: {colocacao}')
print(f'\nCinco PRIMEIROS colocados: {primeiros}')
print(f'\nÚLTIMOS quatro colocados: {ultimos}')
print(f'\nTimes em ordem ALFABÉTICA: {alfabetica}')
print(f'\nO CHAPECOENSE está na {chapecoense}ª posição')
