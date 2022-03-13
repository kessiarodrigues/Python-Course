num = [2, 5, 9, 1]
num[2] = 3
num.append(7)  #adiciona ao fim da lista
num.sort()  #coloca em ordem crescente
num.insert(2, 0)   #na posição 2, adicione 0
num.sort(reverse=True)   #coloca em ordem decrescente
num.pop()   #exclui ultimo elkemento dalista
num.pop(1)   #exclui item 1 da lista
if 2 in num:
    num.remove(2)  #remove o primeiro número 2
print(num)

---------------------------------------------------------------------------------------------------------------------
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for valor in valores:
    print(f'{v}...', end='')

-----------------------------------------------------------------------------------------------------------------
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor')))

