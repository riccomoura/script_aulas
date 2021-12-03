namecar = input('Qual a placa do veículo alugado? ')
kmini = int(input('Qual a quilometragem do veículo no ato da locação? '))
kmfini = int(input('Qual a quilometragem do veículo no ato da entrega? '))
diaria = int(input('Por quantos dias o veículo foi alugado? '))

km = kmfini - kmini
valorkm = km * 0.15
valordiaria = 60 * diaria
valortotal = valordiaria + valorkm

print('O veículo de placa {} foi alugado por {} dias.'.format(namecar, diaria))
print('A quilometragem inicial foi de {}km e a quilometragem final foi de {}.'.format(kmini, kmfini))
print('O total de quilometragem à ser precificada é de {}kms.'.format(km))
print('O valor total da locação é de: R${:.2f}'.format(valortotal))
