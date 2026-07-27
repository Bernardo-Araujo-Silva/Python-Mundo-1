salario = float(input('Digite o salário que recebra o aumento: '))

if salario > 1250:
    print('Você receberá um aumento de 10%, seu novo salário será R$ {:.2f}'.format(salario + salario * 0.10))
else:
    print('Você receberá um aumento de 15%, seu novo salário será R$ {:.2f}'.format(salario + salario * 0.15))