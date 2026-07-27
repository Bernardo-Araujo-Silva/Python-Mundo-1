n1 = float(input('Digite sua primeria nota: '))
n2 = int(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2

print('Sua média foi {:.2f}'.format(m))

if m >= 6:
    print('sua média foi boa, parabéns!')
else:
    print('Sua média foi ruim, estude mais.')
