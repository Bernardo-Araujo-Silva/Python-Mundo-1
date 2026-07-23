m = float(input('Digite uma distância em metros: '))
dec = m * 10
mm = m * 1000
cm = m * 100
km = m / 1000
hm = m / 100
dam = m / 10


print('O valor em milímetros é: {} mm'.format(mm))
print('O valor em centímetros é: {} cm'.format(cm))
print('O valor em decímetros é: {} dm'.format(dec))
print('O valor em quilômetros é: {} km'.format(km))
print('O valor em hectômetros é: {} hm'.format(hm))
print('O valor em decâmetros é: {} dam'.format(dam))