# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

genero = ''
homem = 'Homem'
mulher = 'Mulher'
outro = 'Outro'

while genero != homem[0] and genero != mulher[0] and genero != outro[0]:
  print('[ H ] Homem')
  print('[ M ] Mulher')
  print('[ O ] Outro')
  genero = str(input('Digite o gênero: ')).upper()

if genero == homem[0]:
  genero = homem
elif genero == mulher[0]:
  genero = mulher
elif genero == outro[0]:
  genero = outro

print(f'Gênero: {genero}')
