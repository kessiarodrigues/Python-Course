from math import trunc
n = float(input('Digite um número: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(n, trunc(n)))




from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz e {} é igual a {:.2f}'.format(num, floor(raiz)))

import random
n =random.randint(1, 10)
print(n)
