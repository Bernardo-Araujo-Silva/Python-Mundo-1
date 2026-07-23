import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjascente: '))
h = math.hypot(co, ca)

print('O comprimento da hipotenusa é {:.2f}'.format(h))