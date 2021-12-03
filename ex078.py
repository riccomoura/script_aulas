#Digite 5 valores para inserir em uma lista e mostre o maior e menor valor dela

valores = list ()

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(f'Você digitou os valores {valores}', end='')
print(f' ')

for c in valores:
    print(f'O maior valor foi {max(valores)} na posição {valores.index(max(valores))}')
    print(f'O menor valor foi {min(valores)} na posição {valores.index(min(valores))}')
    break

print('Cheguei ao final da lista')