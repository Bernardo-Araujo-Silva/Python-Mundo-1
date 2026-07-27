dis = float(input('Digite a distância da sua viagem em km: '))

if dis <= 200:
    print('O valor da sua passagem será {:.2f}.'.format(dis * 0.50))
else:
    print('O valor da sua passagem será {:.2f}.'.format(dis * 0.45))