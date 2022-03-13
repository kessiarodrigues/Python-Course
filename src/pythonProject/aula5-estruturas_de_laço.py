nomes = ['Guilhrme', 'Marcelo', 'João', 'Julia']

for x in nomes:
    print (x)

for i in range(4):
    print (nomes[i])


---------------------------------------------------------------------------------------------

i = 0
while i >= 10:
    print ('O numero é menor que 10:', i)
    i = i + 1


-------------------------------------------------------------------------------------------
lista_frutas: ['Maçã', 'Banana', 'Laranja', 'Goiaba', 'Uva']

contador = 0

for fruta in lista_frutas:
    contador +=1

print(contador)

or

print (len(lista_frutas))

---------------------------------------------------------------------------------------------
numero = 0

while True:
    print (numero)
    if numero == 20:
        break
    numero +=2


