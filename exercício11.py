largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
tinta = area / 2
print('A área da parede é {:.2f} m² e a quantidade de tinta necessária é {:.2f} litros.'.format(area, tinta))