from random import randint
from time import sleep
computador = randint(0,5)
jogador = int(input('Digite um número: '))
sleep(3)
if jogador == computador:
    print('Você acertou!')
else:
    print('Você errou.')