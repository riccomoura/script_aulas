soma = 0
cont = 0
cont2 = 0
for c in range(1, 7):
    n = int(input('Digite o {}o valor: '.format(c)))
    cont2 += 1
    if n%2==0:
        soma += n
        cont += 1
print('Você informou {} números totais, sendo {} desses pares e a soma deles = {}.'.format(cont2, cont, soma))