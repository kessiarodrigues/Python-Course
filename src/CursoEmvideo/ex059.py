v1 = int(input('Digite o priemiro valor: '))
v2 = int(input('Digite o Segundo valor: '))

print('''[1]somar
[2]multiplicar
[3]maior
[4]sair do programa''')
menu = int(input('Escolha uma das opções acima: '))

if menu == 1:
    print('O resultado da soma entre {} e {} é {}'.format(v1, v2, v1+v2))
elif menu == 2:
    print('O resultado da multiplicação entre {} e {} é {}'.format(v1, v2, v1*v2))
elif menu == 3:
    if v1 > v2:
        print('{} é maior que {}'.format(v1, v2))
    elif v1 < v2:
        print('{} é maior que {}'.format(v2, v1))
    elif v1 == v2:
        print('Os valores são iguais.')
elif menu == 4:
    print('FIM')
else:
    print('Opção inválida')
