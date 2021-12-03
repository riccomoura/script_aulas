from math import hypot
catop = float(input('Digite a medida do cateto oposto: '))
catadj = float(input('Digite a medida do cateto adjacente: '))
hypotenusa = hypot(catop,catadj)
print('De acordo com as medidas dos catetos, a hipotenusa é de: {:.2f}'.format(hypotenusa))