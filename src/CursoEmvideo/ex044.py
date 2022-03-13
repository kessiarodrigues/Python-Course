valor = float(input('Qual o valor do produto? R$'))
print('-=' * 15)
print('Escolha a condição de pagamento: ')
print('-=' * 15)
print('''[1] A vista no dinheiro ou cheque
[2] A vista no cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão''')
print('-=' * 15)
opcao = int(input('Escolha uma das opções: '))
print('-=' * 15)

if opcao == 1:
    preço = valor - (valor * 10/100)
    print('Essa opção te dá 10% de desconto, você pagará R${:.2f}' .format(preço))
elif opcao == 2:
    preço = valor - (valor * 5/100)
    print('Essa opção te dá 5% de desconto, você pagará R${:.2f}'.format(preço))
elif opcao == 3:
    parcela = valor / 2
    print('Essa opção não te dá nenhum desconto adicional, sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
    parcela = float(input(''))
elif opcao == 4:
    preço = valor + (valor * 20/100)
    parcela = int(input('Em quantas vezes você deseja parcelar? '))
    total = preço / parcela
    print('Essa opção acrescenta 20% de juros ao valor do produto, sua compra será parcelada em {}x de R${:.2f}'.format(parcela, total))
else:
    print('Opção inválida')
