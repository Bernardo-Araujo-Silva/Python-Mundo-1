p = int(input('Digite o preço do produto: R$ '))
d = p * 0.05

print('O preço do produto é R$ {:.2f} e o desconto de 5% é R$ {:.2f}. O preço final com desconto é R$ {:.2f}.'.format(p, d, p - d))