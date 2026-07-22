l= float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))
area = l * a
tinta = area / 2

print('Serão necessários {:.2f} litros de tinta para pintar a parede de {:.2f} m²'.format(tinta, area))