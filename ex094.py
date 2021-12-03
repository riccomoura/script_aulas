#Crie um programa que leia nome, sexo e idade de várias pessoas
#Guarde os dados de cada pessoa em um dicionário
#Guarde todos os dicionários em uma lista
#Mostre>>>
#>>>
#>>
#>
#A) Quantas pessoas foram cadastradas
#B) A média de idade do grupo
#C) Uma lista com todas as mulheres
#D) Uma lista com todas as pessoas com idade acima da média

galera = list()
pessoa = dict()
soma = media = 0

#Cadastro de pessoa
while True:
    pessoa.clear() #Para limpar a lista temporária a cada looping
    pessoa['nome'] = str(input('Nome: '))
    #Validação do gênero
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0] #Só pega o primeiro valor
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.') #else implícito
    #Validação da iade
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    #Teste lógico - deseja continuar?
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.') #else implícito
    if resp == 'N': #else explícito em caso de "N"
        break

#Exibição + validação de gênero feminino
print('-=' * 30)
print(f'Ao todo tempos {len(galera)} pessoas cadastradas.')
media = soma / len(galera) #cálculo da média
print(f'A média de idade é de {media:5.2f} anos.')
print(f'As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('-=' * 30)

#Exibição + validação da lista de pessoas acima da média
print(' <<< LISTA DAS PESSOAS QUE ESTÃO ACIMA DA MÉDIA >>> ')
for p in galera:
    if p['idade'] >= media:
        print(' ')
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
        print()
print()
print(' ++ ENCERRADO ++')



