num = int(input('Digite um número e descubra se ele é par ou impar: '))
resto = num % 2
if resto == 0:
    print('O número {} é par.'.format(num))
else:
    print('O número {} é ímpar.'.format(num))