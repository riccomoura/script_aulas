r1 = float(input('Digite o comprimento de uma reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo.')
else:
    print('Os segmentos acima não podem formar um triângulo.')

print('...')
print('...')
print('...')
print('...')

if r1 == r2 == r3:
    print('Triângulo equilátero.')
elif r1 != r2 != r3:
    print('Triângulo escaleno.')
else:
    print('Triângulo Isósceles.')
