frase = str(input('Escreva uma frase: ')).strip().upper()

print('A sua frase {}...'.format(frase))
print('Possui {} letras A'.format(frase.count('A')))
print('A primeira vez que a letra A aparece é na posição {}'.format(frase.find('A') + 1))
print('E a ultima vez que a lera A aparece é na posição {}'.format(frase.rfind('A') + 1))