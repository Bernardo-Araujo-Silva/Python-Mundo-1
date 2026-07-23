#co = float(input('Digite o comprimento do cateto oposto: '))
#ca = float(input('Digite o comprimento do cateto adjacente: '))
#h = (co ** 2 + ca ** 2) ** (1/2)

#print('O comprimento da hipotenusa é {:.2f}'.format(h))

import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjascente: '))
h = math.hypot(co, ca)

print('O comprimento da hipotenusa é {:.2f}'.format(h))