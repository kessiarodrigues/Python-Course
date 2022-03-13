n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {} e {} a média do aluno é {}'.format(n1, n2, media))

if media < 5:
    print('ALUNO REPROVADO')
elif 7 > media >= 5:
    print('ALUNO EM RECUPERAÇÃO')
elif media >= 7:
    print('ALUNO APROVADO')
