nome = input('Digite seu nome: ')
n = float(input('Digite o valor em Reais que você possui no seu Wallet: '))
n1 = n / 3.27
print('Na carteira de {}, o valor contido em Reais pode ser convertido em {:.2f} dólares.'.format(nome, n1))