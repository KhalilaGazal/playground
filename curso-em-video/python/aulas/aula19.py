"""
pessoas = {'nome': 'Gustavo', 'genero': 'M', 'idade': 22}

print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for keys in pessoas.keys():
    print(keys)

print()

for values in pessoas.values():
    print(values)

print()

del pessoas['genero']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5

for k, v in pessoas.items():
    print(f'{k} = {v}')
    """


"""
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[0])
print(brasil[1]['sigla'])
"""


"""
brasil = list()
estado = dict()

for i in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))

    brasil.append(estado.copy())

print(brasil)

print()

for estado in brasil:
    print(estado)

print()

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')

print()

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
"""
