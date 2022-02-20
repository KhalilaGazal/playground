# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

reta1 = float(input('Digite o comprimento da 1ª reta: '))
reta2 = float(input('Digite o comprimento da 2ª reta: '))
reta3 = float(input('Digite o comprimento da 3ª reta: '))

if abs(reta2 - reta3) < reta1 < (reta2 + reta3) and \
   abs(reta1 - reta3) < reta2 < (reta1 + reta3) and \
   abs(reta1 - reta2) < reta3 < (reta1 + reta2):
    if reta1 == reta2 == reta3:
        triangulo = 'EQUILÁTERO'
    elif reta1 != reta2 != reta3 != reta1:
        triangulo = 'ESCALENO'
    else:
        triangulo = 'ISÓSCELES'
    print(f'Podem formar um triângulo {triangulo}!')
else:
    print('NÃO podem formar triângulo!')
