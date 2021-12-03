#Crie um programa que tenha a função fatorial()
#Receba dois parâmetros: O primeiro indica o número a calcular
#O segundo parâmetro chamado show, que será um valor lógico
#Indique se será mostrado ou não na tela o processo de cálculo do fatorial

#Construindo a função
def fatorial(n, show=False): #por padrão, show recebe FALSE no escopo local
    '''
    = : Calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show: (opcional) mostrar ou não a conta
    :return: O valor do fatorial de um número n.
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#Programa Principal
print(fatorial(5, show=True)) #Parâmetro show recebe TRUE para exibir no escopo global.
help(fatorial) #Help Interactive para exibir as anotações