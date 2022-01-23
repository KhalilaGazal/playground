# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome da cidade: '))

cidade = cidade.lower().split()
santo = 'santo' in cidade[0]

print(f'Começa com "Santo"? {santo}')
