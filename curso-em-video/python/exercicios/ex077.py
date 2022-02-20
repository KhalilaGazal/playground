# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = 'Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Grátis', 'Estudar', 'Praticar', 'Trabalhar',\
           'Mercado', 'Programador', 'Futuro'

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
