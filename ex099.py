#Faça um programa que tenha uma função chamada maior()
#Receba vários parâmetros com valores inteiros
#O Programa tem que analisar todos os valores e dizer qual deles é o maior

from time import sleep

#Iniciando o contador e construindo a função
def maior(* num):
    cont = maior = 0
    print('\nAnalisando os valores passados... ')
    sleep(0.5)
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
#Validando o maior
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


#Programa Principal - testando as possibilidades
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(6)
maior()