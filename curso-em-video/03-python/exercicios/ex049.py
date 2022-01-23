# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

multiplicacao = 0

numero = int(input('Digite um número inteiro: '))

for x in range(1, 11):
    multiplicacao = x * numero
    print(f'{numero} x {x:2} = {multiplicacao}')
