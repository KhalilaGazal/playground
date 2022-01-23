# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

aluno1 = str(input('Digite o nome do PRIMEIRO aluno: '))
aluno2 = str(input('Digite o nome do SEGUNDO aluno: '))
aluno3 = str(input('Digite o nome do TERCEIRO aluno: '))
aluno4 = str(input('Digite o nome do QUARTO aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)

print(f'Aluno escolhido = {escolhido}')
