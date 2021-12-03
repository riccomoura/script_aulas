from random import randint
from time import sleep

#SORTEIO DOS VETORES
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

#ESCOLHA DO JOGADOR E SORTEIO
print('''Suas opções: 
[   0   ] PEDRA
[   1   ] PAPEL
[   2   ] TESOURA''')
print('-=' * 11) #Decoração gráfica
jogador = int(input('Qual é a sua jogada? '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(2)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11) #Decoração gráfica

#LANÇAMENTO DAS ESTRUTURAS CONDICIONAIS ANINHADAS
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VITÓRIA')
    elif jogador == 2:
        print('DERROTA')
    else:
        print('Jogada Inválida')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('DERROTA')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VITÓRIA')
    else:
        print('Jogada Inválida')
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('VITÓRIA')
    elif jogador == 1:
        print('DERROTA')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada Inválida')