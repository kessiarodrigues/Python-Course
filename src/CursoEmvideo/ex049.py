n = int(input('Qual tabuada deseja consultar? '))

for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))
