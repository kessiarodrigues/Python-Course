lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim')
#Tuplas são imutaveis
#lanche[1] = 'arroz' # nao da certo

for comida in lanche:
    print(f'Eu vou comer {comida}')

print(len(lanche)) #comprimento

print(sorted(lanche)) #ordem alfabetica

-------------------------------------------------------------------------------------------
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #apenas junta as duas
print(c)
print(c.count(5)) #quantas vezes aparece o 5
print(c.index(8)) #em que posicão esta o 8

---------------------------------------------------------------------------------
pessoa = ('Késsia', '18', 'F')
del(pessoa) #apaga a tupla da memória
