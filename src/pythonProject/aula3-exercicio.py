idade = int (input ('Digite sua idade: '))
altura = float (input ('Digite sua altura: '))
peso = float (input ('Digite seu peso: '))

if idade >= 18 and altura >= 1.70 and peso >= 60:
    print ('-------------------------')
    print ('Apto a entrar no exercito')
else:
    print ('Não está apto a entrar no exército.')
