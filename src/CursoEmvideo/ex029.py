velocidade = float(input('Qual é a velocidade atual do carro? '))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80KM/h')
    print('Você deve pagar uma multa de {}'.format(multa))
    print('Tenha um bom dia, dirija com segurança.')
else:
    print('Tenha um bom dia e didija com segurança!')