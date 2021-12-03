name = input('Digite o seu nome: ')
celsius = float(input('Agora digite a temperatura em Celsius para calcular a conversão: '))
fahr = (celsius * 9 / 5) + 32
print('{}, a conversão da temperatura {:.1f}c para Fahrenheit resultou em: {:.1f}f'.format(name, celsius, fahr))
