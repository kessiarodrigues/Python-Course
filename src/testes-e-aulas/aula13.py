for c in range(0, 6, -1):
    print('Oi')
    print(c)
print('FIM')


n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f, p):
    print(c)

s = 0
for c in range(0, 3):
    n = int(input('Digite um valor'))
    s = 0 + n
print('A soma dos valores foi {}'.format(s))


