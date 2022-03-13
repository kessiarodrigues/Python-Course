try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except:
    print('Infelizmente tivemos uma falha.')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre!')
