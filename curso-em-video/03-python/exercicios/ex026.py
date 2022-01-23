# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

nome = str(input('Digite a frase: ')).strip()

nome = nome.lower()
qtd = nome.count('a')
primeiro = nome.find('a') + 1
ultimo = nome.rfind('a') + 1

print(f'Letra A aparece {qtd} vez(es) na frase.')
print(f'Primeira letra A aparece na {primeiro}ª posição.')
print(f'Última letra A aparece na {ultimo}ª posição.')
