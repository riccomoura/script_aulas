n = int(input('Digite um número para retornar sua tabuada: '))
for c in range(0, 11):
    print('{} x {} = {}'.format(n, c, n*c))

#Método de corno:

'''  
n = int(input('Digite um número para retornar sua tabuada: '))
for c in range(0, 11):
    res = n * c
    print('{} x {} = {}'.format(n, c, n * c))  
'''