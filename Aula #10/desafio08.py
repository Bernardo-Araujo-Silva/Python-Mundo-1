a = float(input('Digite o comprimeto da primeira reta: '))
b = float(input('Digite o comprimeto da segunda reta: '))
c = float(input('Digite o comprimeto da terceira reta: '))

if a + b > c:
    if a + c > b:
        if b + c > a:
            print('Pode formar um triângulo')
        else:
            print('Não pode formar um triângulo')
    else:
        print('Não pode formar um triângulo')
else:
    print('Não pode formar um triângulo')