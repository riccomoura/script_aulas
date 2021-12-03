#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios
#Guarde esses resultados em um dicionário
#No final, coloque esse dicionário em ordem, sabendo que:
#O vencedor tirou o maior número do dado

from random import randint
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)
        }

#Uso do itemgetter, do método operator, para ordenar por elemento da sublista
ranking = dict()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {k} no dado.')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

#Rankeamento
print('-=' * 30)
print(' <<< RANKING DOS JOGADORES >>> ')
for i, v in enumerate(ranking):
    print(f'   {i+1} lugar: {v[0]} com {v[1]}')