#Crie um programa que vai ler vários números e colocar em uma lista
#Crie duas listas extras que vão conter apenas os valores pares e impares
#Ao final, mostre o conteúdo das três listas geradas

num = list()
#Criando as listas extras
pares = list()
impares = list()

while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar? [S/N] ')).upper()
    if resp in 'Nn':
        break
    print(num)

    for i, v in enumerate(num):
        if v % 2 == 0: #verificando e atribuindo pares e impares
            pares.append(v)
        elif v % 2 == 1:
            impares.append(v)
    print('-=' * 30)
    print(f'A lista completa é {num}')
    print(f'A lista de pares é {pares}')
    print(f'A lista de impares é {impares}')