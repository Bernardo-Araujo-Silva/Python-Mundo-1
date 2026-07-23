v = float(input('Qual o valor do produto? R$'))
d = v * 0.05

print('O produto que custa R${:.2f} sairá por R${:.2f} com 5% de desconto'.format(v, v - d))