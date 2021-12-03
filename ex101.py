#Crie um programa que tenha uma função chamada voto()
#Receba como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
#Indique se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições

#Usando escopo de importação

'''
Usando escopo de importação, se importa uma função como datetime unicamente para dentro da
função de interesse. Assim se economiza memória na execução.
'''

#Construindo a função usando escopo de importação
def voto(ano):
    from datetime import date #escopo de importação para economizar memória
    atual = date.today().year #extraindo data atual
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos, você NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos, seu voto é OPCIONAL'
    else:
        return f'Com {idade} anos, seu voto é OBRIGATÓRIO'


#Programa Principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc)) #imprime a função a partir do dado de entrada "nasc"