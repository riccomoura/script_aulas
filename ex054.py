from datetime import date

atual = date.today().year
totmaior = 0
totcoroa = 0
totmenor = 0

for pess in range(1, 8):
    nasc = int(input('Em que ano a {}a nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 18 and idade < 65:
        totmaior += 1
    elif idade >= 65:
        totcoroa += 1
    else:
        totmenor += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas da melhor idade'.format(totcoroa))
print('Ao todo tivemos {} pessoas menores de idade'.format(totmenor))

