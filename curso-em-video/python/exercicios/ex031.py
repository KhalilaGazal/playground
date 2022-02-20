# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Digite a distância da viagem em quilômetros: '))

taxa = .5 if distancia <= 200 else .45
preco = distancia * taxa

print(f'Preço da passagem = R${preco:.2f}')
