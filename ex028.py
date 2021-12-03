import random
print('O computador está pensando em um número.')
print('... pensando...')
print('... consegue adivinhar?')
r = 1
a = 2
n = 3
d = 4
o = 5
lista = [r, a, n, d, o]
num = int(input('Escolha um número de 1 a 5: '))
sorteio = random.choice(lista)
if num == sorteio:
    print('Você acertou, o número é {}'.format(sorteio))
else:
    print('Você errou, tente novamente.')

#from random import randint
#computador = randint(0,5)
#jogador = int(input('Digite um número: '))
#if jogador == computador:
#    print('Você acertou!')
#else:
#    print('Você errou.')