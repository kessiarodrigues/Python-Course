n = int(input('Me diga um número qualquer: '))
resultado = n % 2
if resultado == 1:
    print('O número {} é IMPAR'.format(n))
else:
    print('O número {} é PAR'.format(n))
