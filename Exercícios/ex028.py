from random import randint
from time import sleep

pc = randint(0, 5)
user = int(input('Escolha um número entre 0 e 5 e veja se adivinha qual o computador vai gerar: '))

print('O número que você escolheu foi {}'.format(user))
print('O número sorteado foi')
print('...')
sleep(3)
print('{}'.format(pc))


if user == pc:
    print('Parabés, você acertou o número!!!')
else:
    print('Não foi dessa vez, tente novamente...')