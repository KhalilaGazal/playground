# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o valor do salário: '))

aumento = .15
novo_salario = salario + (salario * aumento)

print(f'Salário com 15% de aumento = R${novo_salario:.2f}')
