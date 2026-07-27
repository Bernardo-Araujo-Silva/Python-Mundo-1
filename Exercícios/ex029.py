vel = int(input('Digite a velocidade do veículo: '))
excesso = vel - 80
multa = excesso * 7


if vel <= 80:
    print('Boa viagem!')
else:
    print('Você vai receber uma multa.')
    print('A multa será de R$ {:.2f}.'.format(multa))