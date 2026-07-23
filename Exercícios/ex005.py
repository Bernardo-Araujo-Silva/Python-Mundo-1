n = int(input('Digite um numero:' ))
a = n - 1
s = n + 1

print('O antecessor de {} é {} e o sucessor é {}'.format(n, a, s))

# Se não precisar exibir os valores futuaramente ou deseja economizar memória, pode ser feito assim:

n = int(input('Digite um numero:' ))

print('O antecessor de {} é {} e o sucessor é {}'.format(n, (n-1), (n+1)))