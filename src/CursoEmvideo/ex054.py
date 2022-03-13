from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for pess in range(1, 8):
    nasc = str(input('Em que ano a pessoa {} nasceu?'.format(c)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivems {} pessoas menores de idade'.format(totmenor))
