# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

msg = ''

ano = int(input('Digite o ano ou digite 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year
if not (ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0):
    msg = ' NÃO'

print(f'{ano}{msg} é um ano bissexto.')
