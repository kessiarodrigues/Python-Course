teste = list()
teste.append('Késsia')
teste.append(18)
galera = list()
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 22
print(galera)
-------------------------------------------------------------------------------------------------------------
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
for p in galera:
    print(p[0])
    ------------------------------------------------------------------------------------------------------------
galera = list
dado = list
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[] >= 21:
        print(f'{p[0]}, é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temnos {totmai} maiores e {totmen} menores de idade.')
