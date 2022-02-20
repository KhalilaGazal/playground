# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o valor do salário: '))

if salario > 1250:
    porcento = .10
else:
    porcento = .15

novo_salario = salario + (salario * porcento)
aumento = novo_salario - salario

print(f'Aumento = R${aumento:.2f}\nNovo salário = R${novo_salario:.2f}')
