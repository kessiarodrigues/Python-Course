import math
CO = float(input('Comprimento do catet oposto: '))
CA = float(input('Cpmprimento do cateto adjacente: '))
h = math.hypot(CO, CA)
print("A hipotenusa vai medir {:.2f}".format(h))
