# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
golsPartida = list()
golsTotal = 0

jogador['nome'] = str(input('Nome: '))
jogador['partidas'] = int(input('Partidas: '))

for i in range(0, jogador['partidas']):
    partida = int(input(f'Gols da {i+1}ª partida: '))
    golsTotal += partida
    golsPartida.append(partida)

jogador['golsPartida'] = golsPartida
jogador['golsTotal'] = golsTotal

print(f'\n{jogador.items()}\n')

for k, v in jogador.items():
    print(f'{k}: {v}')
print()

print(f'Jogador {jogador["nome"]} jogou {jogador["partidas"]} partida(s).')
for i in range(0, jogador['partidas']):
    print(f'Na {i+1}ª partida fez {golsPartida[i]} gol(s).')
print(f'Um total de {golsTotal} gols.')
