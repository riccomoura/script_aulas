from time import sleep
print('=== TESTE DE COMPARAÇÃO ENTRE NÚMEROS ===')

sleep(1)

num1 = int(input('Digite um número inteiro "x": '))
num2 = int(input('Digite outro número inteiro "y": '))

print('Processando...')
sleep(1)

if num2 > num1:
    print('O número inteiro {} é maior que o número {}'.format(num2, num1))
elif num1 > num2:
    print('O número inteiro {} é maior que o número {}'.format(num1, num2))
else:
    print('Os números atribuídos a "x" e "y" são iguais.')
    sleep(1)
    print('{} e {} possuem o mesmo valor.'.format(num1, num2))

