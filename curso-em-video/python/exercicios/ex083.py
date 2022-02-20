# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

lista = []

expressao = str(input('Digite a expressão: '))

for i in expressao:
    if i == '(':
        lista.append('(')
    elif i == ')':
        if len(lista) == 0:
            lista.append(')')
            break
        else:
            lista.pop()

if len(lista) == 0:
    print('Expressão VÁLIDA!')
else:
    print('Expressão INVÁLIDA!')
