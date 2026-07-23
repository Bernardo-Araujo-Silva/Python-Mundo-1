r = float(input('Quantos reais você tem? R$'))
d = r / 5.08
e = r / 5.78

print('Com seus R${:.2f} você pode comprar US${:.2f}'.format(r, d))
print('Com seus R${:.2f} você pode comprar €{:.2f}'.format(r, e))