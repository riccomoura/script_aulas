from time import sleep
from datetime import date

data_atual = date.today()
data = '{}'.format(data_atual.year)

print('=== CASAS PYTHONHAS - ANO DE {} ==='.format(data_atual.year))
sleep(1)
print('...')
sleep(1)

print('>>>>> TERMINAL DE CÁLCULO PARA CONDIÇÕES ESPECIAIS <<<<<')
sleep(1)
cost = float(input('\nDigite o valor do produto: R$'))
sleep(1)
print('Muito bem, o valor inserido para o produto foi de R${:.2f}'.format(cost))
sleep(2)
cond = int(input('\nEscolha a condição para o cálculo:\n>>> À vista em dinheiro ou cheque: (1)\n>>> À vista no cartão: (2)\n>>> Em até 2x no cartão: (3)\n>>> Em 3x parcelas ou mais no cartão: (4)\n>>> Digite para escolher: '))
sleep(1)
np = int(input('\nQuantas parcelas? Limite de 12 prestações: '))

numpar = np
vf1 = cost * 0.90
vf2 = cost * 0.95
vf3 = cost / 2
vf4 = cost * 1.20
vf4par = vf4 / np

if cond == 4:
    print('Numero de parcelas selecionadas: {}'.format(numpar))
    sleep(2)
    print('O valor do produto parcelado em {} prestações terá 20% de valor acrescido.'.format(numpar))
    sleep(2)
    print('Subtotal: R${:.2f}\nO valor de cada parcela será de: R${:.2f}'.format(vf4, vf4par))
elif cond == 1:
    sleep(2)
    print('O valor de R${} sob o produto terá um desconto aplicado de 10%.\nSubtotal: R${:.2f}'.format(cost, vf1))
elif cond == 2:
    sleep(2)
    print('O valor de R${} sob o produto terá um desconto aplicado de 5%.\nSubtotal: R${:.2f}'.format(cost, vf2))
else:
    sleep(2)
    print('O parcelamento em duas vezes sem juros não afetará o valor final.')
    sleep(2)
    print('Subtotal: R${}\nO valor de cada parcela será de: R${:.2f}'.format(cost, vf3))