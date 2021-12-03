nome = str(input('Digite o seu nome: '))
salario = float(input('Digite seu atual salário: '))

if salario <= 1250.00:
    print('Seu novo salário reajustado será de: R${:.2f}'.format(salario*1.10))
else:
    print('Seu novo salário será de: R${:.2f}'.format(salario*1.15))

print('Parabéns pelo seu novo salário, {}. Foi mais que merecido!'.format(nome))