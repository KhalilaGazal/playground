# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

aluno1 = str(input('Digite o nome do PRIMEIRO aluno: '))
aluno2 = str(input('Digite o nome do SEGUNDO aluno: '))
aluno3 = str(input('Digite o nome do TERCEIRO aluno: '))
aluno4 = str(input('Digite o nome do QUARTO aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)

print(f'Ordem de apresentação = {lista}')
