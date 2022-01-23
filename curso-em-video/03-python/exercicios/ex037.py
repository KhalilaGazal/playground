# Escreva um programa em Python que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um número inteiro: '))
print('''Base de converão
[ 0 ] Binário
[ 1 ] Octal
[ 2 ] Hexadecimal''')
escolha = int(input('Escolha uma opção: '))

opcao = ['Binário', 'Octal', 'Hexadecimal']

if escolha != 0 and escolha != 1 and escolha != 2:
    print('Opção inválida! Tente novamente!')
else:
    if escolha == 0:
        conversao = bin(numero)[2:]
    elif escolha == 1:
        conversao = oct(numero)[2:]
    else:
        conversao = hex(numero)[2:]
    print(f'{numero} em {opcao[escolha]} = {conversao}')
