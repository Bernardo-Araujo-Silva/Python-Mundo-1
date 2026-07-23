from math import radians, sin, cos, tan

a = int(input('Digite um ângulo qualquer: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))

print('O ângulo de {} tem o SENO de {:.2f}'.format(a, s))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a, c))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(a, t))