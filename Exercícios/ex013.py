s = float(input('Qual o salário do funcionário? R$'))
a = s * 0.15

print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(s, s + a))