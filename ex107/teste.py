from ex107 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade do {p} é R${moeda.metade(p)}.')
print(f'O dobro de {p} é R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Diminuindo 25%, temos {moeda.diminuir(p, 25)}')