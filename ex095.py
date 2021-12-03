#Aprimore o exercicio093>>>

# <<<  Crie um programa que gerencie o aproveitamento de um jogador de futebol
#      O programa vai ler o nome do jogador e quantas partidas ele jogou
#      Depois, vai ler a quantidade de gols feitos em cada partida
#      No final, tudo isso será guardado em um dicionário
#      Inclua o total de gols feitos durante o campeonato

#Faça-o funcionar com vários jogadores
#Inclua um sistema de visualização de detalhes do aproveitamento

#Construindo o dicionário
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear() #limpando lista temporária a cada looping
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear() #limpando partidas jogadas a cada looping de novo jogador inserido
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}?')))
    jogador['gols'] = partidas[:] #copiando dados de partidas para gols, sendo [:] pois partidas é lista
    jogador['total'] = sum(partidas) #somando partidas
    time.append(jogador.copy()) #copiando jogador para time, sendo copy() por time ser um dicionário
    #Validação de Sim e Não
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break

#Exibição do nome do jogador
print('-' * 40)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)

#Exibição ordenada
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

#Validação a opção de parar a inserção + exibição final
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'  No jogo {i+1} fez {g} gols.')
        print('-' * 40)
    print('VOLTE SEMPRE')