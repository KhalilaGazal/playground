n1 = float(input('Digite  a primeira nota: '))
n2 = float(input('Digite  a segunda nota: '))
media = (n1 + n2) / 2
print(f'A sua média foi {media:.1f}')
print('Parabéns!' if media >= 6 else 'Estude mais!')

'''if media >= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi ruim! Estude mais!')'''
