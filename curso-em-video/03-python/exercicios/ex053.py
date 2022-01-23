# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO,
# ANOTARAM A DATA DA MARATONA.

from unidecode import unidecode

palindromo = True
replace = ' "“”,;.!?-:|\/@#+§$%&*_()[]{}~'

input = str(input('Digite a frase: ')).strip()
frase = input

for r in replace:
    frase = frase.replace(r, '')
frase = unidecode(frase.lower())
inverso = frase[::-1]
letras = len(frase)

for i in range(0, letras):
    if not frase[i] == inverso[i]:
        palindromo = False
        break
if palindromo:
    print(f'"{input}" é um PALÍNDROMO!')
else:
    print(f'"{input}" NÃO é um palíndromo!')
