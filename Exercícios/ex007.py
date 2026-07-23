n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2

print('A média entre {} e {} é igual à {:.2f}'.format(n1, n2, m))

# Se não precisar exibir os valores futuaramente ou deseja economizar memória, pode ser feito assim:

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

print('A média entre {} e {} é igual à {:.2f}'.format(n1, n2, (n1 + n2) / 2))