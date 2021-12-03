from datetime import date
from time import sleep
sleep(1)

nome = str(input('Identifique-se, atleta. Digite seu nome: '))
nasc = int(input('Digite o ano de nascimento: '))
data_atual = date.today()
anoatual = '{}'.format(data_atual.year)
idade = data_atual.year - nasc


if idade <= 9:
    print('Categoia mirim.')
elif 9 < idade <= 14:
    print('Categoria infantil.')
elif 14 < idade <= 19:
    print('Categoria Junior.')
elif 19 < idade <= 20:
    print('Categoria Senior.')
else:
    print('Categoria Master.')