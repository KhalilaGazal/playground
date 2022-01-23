lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita'

for comida in lanche:
    print(f'Eu vou comer {comida}')

for i, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {i}')

for i in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[i]} na posição {i}')

print(sorted(lanche))


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(a)
print(b)
print(c)
print(d)

print(len(c))
print(d.count(5))
print(d.index(8))
print(d.index(5, 1))


pessoa = 'Gustavo', 39, 'H', 99.88
del(pessoa)
print(pessoa)
