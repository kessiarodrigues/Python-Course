real = float(input('Quanto dinheiro você tem na carteira? R$'))

dólar = real / 5.29

print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dólar))
