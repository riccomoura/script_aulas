n = int(input('Digite um número e descubra seu dobro, triplo e raíz quadrada: '))
n1 = n * 2
n2 = n * 3
n3 = n ** (1/2)
print('O dobro de {} é {},\n O triplo de {} é {},\n E a raíz quadrada de {} é {:.2f}.\n Incrível, não é mesmo?'.format(n, n1, n, n2, n, n3))