#Faça um programa que tenha uma lista chamada numeros()
#Também tenha duas funções chamadas sorteia() e somaPar()
#A função sorteia() vai sortear 5 números e colocar dentro da lista
#A função somaPar() vai mostrar a soma entre todos os valores pares sorteados

from random import randint

#Definindo e construindo a função sorteia()
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10) #sorteando 5 valores entre 1 e 10
        lista.append(n)
        print(f' {n}', end='')
    print('\nPRONTO')


def somaPar(lista):
    soma = 0 #Iniciando a soma
    for valor in lista:
        if valor % 2 == 0: #Teste lógico e validação de números pares
            soma += valor #somando os valores pares
    print(f'Somando os valores pares de {lista}, temos {soma}.')
    print(f'FIM')

#Programa Principal
numeros = list() #numeros são guardados na lista
sorteia(numeros) #função opera em números após ele guardar os valores da lista
somaPar(numeros)