num = int(input('Informe um número: ')).strip()
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('minhar: {}'.format(m))
print('centena: {}'.format(c))
print('dezena: {}'.format(d))
print('unidade: {}'.format(u))