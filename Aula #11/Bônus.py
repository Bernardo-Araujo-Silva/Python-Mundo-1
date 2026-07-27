from time import sleep

# CORES
# STYLES - 0, 1, 4, 7
# TEXT - 31, 32, 33, 34, 35, 36, 37
# BACKGROUND - 40, 41, 42, 43, 44, 45, 46, 47

# Cores do texto
print('Cores do texto')
sleep(1)

print('\033[30mPreto\033[m')
sleep(0.5)
print('\033[31mVermelho\033[m')
sleep(0.5)
print('\033[32mVerde\033[m')
sleep(0.5)
print('\033[33mAmarelo\033[m')
sleep(0.5)
print('\033[34mAzul\033[m')
sleep(0.5)
print('\033[35mRoxo\033[m')
sleep(0.5)
print('\033[36mCiano\033[m')
sleep(0.5)
print('\033[37mCinza\033[m')

sleep(1)
print('-=-' * 20)

# Cores de fundo
print('Cores de fundo')
sleep(1)

print('\033[40mFundo preto\033[m')
sleep(0.5)
print('\033[41mFundo vermelho\033[m')
sleep(0.5)
print('\033[42mFundo verde\033[m')
sleep(0.5)
print('\033[43mFundo amarelo\033[m')
sleep(0.5)
print('\033[44mFundo azul\033[m')
sleep(0.5)
print('\033[45mFundo roxo\033[m')
sleep(0.5)
print('\033[46mFundo ciano\033[m')
sleep(0.5)
print('\033[47mFundo cinza\033[m')

sleep(1)
print('-=-' * 20)

# Estilos
print('Estilos')
sleep(1)

print('\033[0mTexto normal\033[m')
sleep(0.5)
print('\033[1mTexto em negrito\033[m')
sleep(0.5)
print('\033[4mTexto sublinhado\033[m')
sleep(0.5)
print('\033[7mCores invertidas\033[m')

sleep(1)
print('-=-' * 20)

print('Todas as combinações')
sleep(1)

for texto in range(30, 38):
    for fundo in range(40, 48):
        print('\033[{};{}m Texto {} com fundo {} \033[m'.format(
            texto, fundo, texto, fundo
        ))
        sleep(0.1)

sleep(1)
print('-=-' * 20)

print('Todos os estilos')
sleep(1)

for estilo in [0, 1, 4, 7]:
    for texto in range(30, 38):
        for fundo in range(40, 48):
            print('\033[{};{};{}m Estilo {} | Texto {} | Fundo {} \033[m'.format(
                estilo, texto, fundo, estilo, texto, fundo
            ))
            sleep(0.05)

sleep(1)
print('-=-' * 20)

print('Alguns exemplos prontos')
sleep(1)

print('\033[1;31mVermelho em negrito\033[m')
sleep(0.5)
print('\033[4;32mVerde sublinhado\033[m')
sleep(0.5)
print('\033[1;33;44mAmarelo em negrito com fundo azul\033[m')
sleep(0.5)
print('\033[1;37;41mBranco em negrito com fundo vermelho\033[m')
sleep(0.5)
print('\033[7;34mAzul com cores invertidas\033[m')

sleep(1)
print('-=-' * 20)

print('Para colorir apenas uma parte da frase')
sleep(1)

nome = 'Bernardo'

print('Olá, \033[34m{}\033[m! Seja bem-vindo.'.format(nome))