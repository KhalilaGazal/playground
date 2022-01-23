# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

opcao = 0

numero1 = float(input('Digite o 1º número: '))
numero2 = float(input('Digite o 2º número: '))

while opcao != 5:
    print('=' * 20)
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair do programa')
    opcao = float(input('Escolha uma opção: '))
    if opcao == 1:
        soma = numero1 + numero2
        print('SOMA')
        print(f'{numero1} + {numero2} = {soma}')
    elif opcao == 2:
        multiplicacao = numero1 * numero2
        print('MULTIPLICAÇÃO')
        print(f'{numero1} x {numero2} = {multiplicacao}')
    elif opcao == 3:
        if numero1 > numero2:
            print(f'MAIOR número = {numero1}')
        elif numero2 > numero1:
            print(f'MAIOR número = {numero2}')
        else:
            print('Os dois números são IGUAIS!')
    elif opcao == 4:
        numero1 = float(input('Digite o 1º número: '))
        numero2 = float(input('Digite o 2º número: '))
    elif opcao == 5:
        print('Programa finalizado com sucesso!')
    else:
        print('Opção inválida! Por favor, tente novamente.')
