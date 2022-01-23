# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

termo = int(input('Digite o 1º termo: '))
razao = int(input('Digite a razão: '))

count = 1
qtd = 10
total = 0

while qtd != 0:
    total += qtd
    while count <= total:
        print(termo, end='')
        print(' - ' if termo != total else '', end='')
        termo += razao
        count += 1
    qtd = int(input('\nQuantos termos mais deseja mostrar? (Digite 0 para parar) '))

print(f'Total de termos = {total}')
