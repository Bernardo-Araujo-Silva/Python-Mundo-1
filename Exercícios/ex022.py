nome = str(input('Digite seu nome completo: ')).strip()

print('Olá {}...'.format(nome))
print('Seu nome com todas as letras maiúsculas fica assim: {}.'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas fica assim: {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))