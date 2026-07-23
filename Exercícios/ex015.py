d = int(input('Por quantos dias você alugou o carro? '))
km = float(input('Quantos km você rodou com o carro? '))
vd = d * 60
vk = km * 0.15

print('O valor do aluguel do carro se baseia em R$60,00 por dia e R$0,15 por km rodado')
print('=' * 100)
print('Você ficou {} dias com o carro e rodou {:.2f}km com o carro'.format(d, km))
print('Sabendo disso, o valor a ser pago pelo carro é de R${:.2f}'.format(vd + vk))