#Crie um programa que gerencie o aproveitamento de um jogador de futebol
#O programa vai ler o nome do jogador e quantas partidas ele jogou
#Depois, vai ler a quantidade de gols feitos em cada partida
#No final, tudo isso será guardado em um dicionário
#Inclua o total de gols feitos durante o campeonato

#Construindo o dicionário
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Digite o nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c+1}?' )))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas) #somar os gols de cada partida
print('-=' * 30)
print(jogador)
print('-=' * 30)

#Construindo a exibição
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

for i, v in enumerate(jogador['gols']):
    print(f' => na partida {i+1} fez {v} gols.')
print()
print(f'Foi um total de {jogador["total"]} gols.')