pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
del pessoas['sexo'] #deleta
pessoas['nome'] = 'Késsia' #troca gustavo por kessia
pessoas['peso'] = 55 #adiciona key e seu valor

for k, v in pessoas.items:
    print(f'{k} = {v}')
------------------------------------------------------------------------------------------------------------------
#dicionrio dentro de lista
brasil = list
estado1 = {'uf': 'Rio de janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])
--------------------------------------------------------------------------------------------------------------
estado = dict
brasil = list
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy)
for e in brasil:
    for k, v in e.items():
        print(f'{k}, {v}')
        