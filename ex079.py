#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista
#Caso o número já exista, ele não pode ser adicionado
#No final, exiba em ordem crescente os valores únicos

valores = list()

while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado! Não é possível adicionar.')
    opt = input('Deseja continuar? [S/N] ').strip().upper()
    if opt == "N":
        break
    else:
        continue
valores.sort()
print(valores)