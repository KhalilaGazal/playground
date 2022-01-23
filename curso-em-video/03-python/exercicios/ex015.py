# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dia = int(input('Digite a quantidade de dias alugados: '))
km = float(input('Digite a quantidade de quilômetros rodados: '))

preco = (60 * dia) + (.15 * km)

print(f'Preço a pagar = R${preco:.2f}')
