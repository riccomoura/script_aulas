from time import sleep
print('Este programa exibirá a soma dos números ímpares\nmúltiplos de três\nEntre 1 e 500...')
sleep(2)
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c %3 == 0:
        cont += 1
        soma += c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))