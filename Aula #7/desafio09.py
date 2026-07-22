s = float(input('Digite o salário do funcionário: R$ '))
a = s * 0.15
ns = s + a

print('O salário do funcionário era R$ {:.2f}, com o aumento de 15% ele passará a receber R$ {:.2f}.'.format(s, ns))