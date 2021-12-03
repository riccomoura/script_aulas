#Análise de Dados em uma Tupla

# Transformar em tupla:

num = (int(input('Digite um número: ')),
        int(input('Digite um número: ')),
        int(input('Digite um número: ')),
        int(input('Digite um número: '))
       )
print(f'Você digitou os valores {num}')

#A) Contar os números 9 exibidos

print(f'O valor 9 apareceu {num.count(9)} vezes')

#B) A posição do número 3 na tupla

if 3 in num:
    print(f'O valor de 3 apareceu na {num.index(3)+1}a posição.')
else:
    print('O valor 3 não foi digitado.')

#C) Informar a quantidade de números pares:
print(f'Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
