# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Digite um número inteiro: '))

r1 = 1 * n
r2 = 2 * n
r3 = 3 * n
r4 = 4 * n
r5 = 5 * n
r6 = 6 * n
r7 = 7 * n
r8 = 8 * n
r9 = 9 * n
r10 = 10 * n

print('=' * 15)
print(f'Tabuada do {n}')
print('-' * 15)
print(f'{n} x {1:2} = {r1}')
print(f'{n} x {2:2} = {r2}')
print(f'{n} x {3:2} = {r3}')
print(f'{n} x {4:2} = {r4}')
print(f'{n} x {5:2} = {r5}')
print(f'{n} x {6:2} = {r6}')
print(f'{n} x {7:2} = {r7}')
print(f'{n} x {8:2} = {r8}')
print(f'{n} x {9:2} = {r9}')
print(f'{n} x {10:2} = {r10}')
print('=' * 15)
