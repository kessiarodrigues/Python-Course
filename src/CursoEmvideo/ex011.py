larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt

print('Sua parede tem a dimensão de {}X{} e sua área é de {} m².'.format(larg, alt, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(area / 2))

# cada 2 m² de parede precisa de 1 litro de tinta