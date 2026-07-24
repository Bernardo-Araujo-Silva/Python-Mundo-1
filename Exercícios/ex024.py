cidade = str(input('Digite a cidade que você nasceu: ')).strip()

print('A sua cidade natal é {}'.format(cidade))
print('Sua cidade começa com santo? {}'.format(cidade[:5].upper() == 'SANTO'))