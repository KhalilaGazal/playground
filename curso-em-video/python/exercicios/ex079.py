# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = list()

while True:
    flag = ' '

    numero = int(input(f'Digite um número: '))
    if numero in lista:
        print('Valor NÃO será adicionado porque já está na lista.')
    else:
        lista.append(numero)
        print('Valor adicionado!')

    while flag not in 'sn':
        flag = str(input('Quer continuar? [S/N] ')).lower()
    if flag == 'n':
        break

lista.sort()
print(f'Valores digitados: {lista}')
