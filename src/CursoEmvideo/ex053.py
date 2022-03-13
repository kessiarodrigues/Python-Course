frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} ´{}'.format(junto, inverso))
if inverso == junto:
    print('Temos um políndromo!')
else:
    print('A frase digitada não é um políndromo!')
