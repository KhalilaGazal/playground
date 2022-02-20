# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
dados = list()
golsPartida = list()
golsTotal = codigo = opcao = 0
flagOpcao = 999

while True:
    flag = ' '

    codigo += 1
    jogador['codigo'] = codigo
    jogador['nome'] = str(input('Nome: '))
    jogador['partidas'] = int(input('Partidas: '))

    for i in range(0, jogador['partidas']):
        partida = int(input(f'Gols da {i+1}ª partida: '))
        golsTotal += partida
        golsPartida.append(partida)

    jogador['golsPartida'] = golsPartida
    jogador['golsTotal'] = golsTotal

    dados.append(jogador.copy())

    while flag not in 'sn':
        flag = str(input('Quer continuar? [S/N] ')) .lower()
    if flag == 'n':
        break

for k in jogador.keys():
    print(f'{k} | ', end='')
print()
print('-' * 50)

for jogador in dados:
    for v in jogador.values():
        print(f'{v} | ', end='')
    print()

print()
while opcao != flagOpcao:
    opcao = int(input(f'Digite um código (ou {flagOpcao} para parar): '))


