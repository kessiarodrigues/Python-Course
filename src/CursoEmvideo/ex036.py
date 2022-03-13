valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos a anos de financiamento? '))
prestação = valor / (anos * 12)

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor, anos, prestação))

if prestação > salario * (30 / 100):
    print('EMPRÉSTIMO NEGADO')
else:
    print('Empréstimo concedido!')
