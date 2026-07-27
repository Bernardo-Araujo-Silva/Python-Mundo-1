a = float(input('Digite o comprimeto da primeira reta: '))
b = float(input('Digite o comprimeto da segunda reta: '))
c = float(input('Digite o comprimeto da terceira reta: '))

if a + b > c:
    if a + c > b:
        if b + c > a:
            print('Esses comprimentos de retas podem formar um triângulo!')
        else:
            print('Não é possivel formar um triângulo com essas medidas.')
    else:
        print('Não é possivel formar um triângulo com essas medidas.')
else:
    print('Não é possivel formar um triângulo com essas medidas.')