#Faça um programa que tenha uma função chamada contador()
#Receba três parâmetros: início, fim e passo
#Seu programa tem que realizar três contagens através da função criada
#O programa deve reconduzir um passo inserido como ZERO para passo 1
#O programa deve funcionar para contagens regressivas e progressivas
from time import sleep

#Definindo e construindo a função contador()
def contador(i, f, p): #inicio, fim e passo
    #Teste Lógico para validar passo zerado e negativo
    if p < 0: #verificar se o passo é positivo
        p *= -1
    if p == 0: #transformar o passo ZERO em passo 1
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(2.5)

#Teste de Validação
    if i < f: #condicional para contagem progressiva
        cont = i #Se início for menor que fim, contador recebe inicio
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p #contador iniciado na regra do passo
        print('FIM')
    else: #condicional para contagem regressiva
        cont = i
        while cont >= f:
            print(f'{cont}', end='')
            sleep(0.5)
            cont -= p
        print(f'FIM')
        print('-=' * 40)

#Programa Principal
contador(1, 10, 1)
contador(10, 1, 1)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início:   '))
fim = int(input('Fim:      '))
pas = int(input('Passo:    '))
contador(ini, fim, pas)