l = float(input('Qual a largura da parede? '))
a = float(input('Qual a altura da parede? '))
area = l * a

print('A dimensão da parede seria {:.2f} x {:.2f} e sua área seria de {:.2f}m²'.format(l, a, area))
print('Para pintar a parede serão usados {:.2f} litros de tinta'.format(area / 2))