print('==== PREÇO DA PASSAGEM RYAN AIR ====')
km = float(input('Digite a quilometragem da viagem: '))
pay1 = 0.50
pay2 = 0.45
if km < 200:
    print('O valor da passagem é de R${:.2f}'.format(km*pay1))
else:
    print('O valor da passagem é de R${:.2f}'.format(km*pay2))