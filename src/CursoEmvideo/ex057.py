sexo = str(input('Informe seu sexo [M/F]:')).strip().upper()[0]
while sexo not in 'MFfm':
    sexo = str(input('Dados inválidos, por favor, informe seu sexo [M/F]: '))
print('Sexo {} registrado com sucesso.'.format(sexo))


