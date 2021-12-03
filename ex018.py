from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo para descobrir seu seno, cosseno e tangente: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('Para este ângulo, temos o seno de {:.2f}, o cosseno de {:.2f} e a tangente de {:.2f}'.format(seno, cosseno, tangente))