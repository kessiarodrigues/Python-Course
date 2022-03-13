nome = str(input('Qual é seu nome?: '))
if nome == 'Késsia':
    print('Que nome lindo!')
elif nome == 'Lucas':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Maria Julia Patricia':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
