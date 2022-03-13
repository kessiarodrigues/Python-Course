from random import randint
computador = randint(0, 10)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
while jogador != computador:
    chance  = input('Incorreto! Eu pensei no número {}. Tente novamente: '.format(computador))
    computador = randint(0, 10)
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')

