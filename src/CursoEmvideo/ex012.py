preço = float(input('Qual é o preço do produto? R$'))
novo = preço * 5/100
desconto = preço - novo

print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, desconto))

