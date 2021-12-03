#Insira números em uma lista que automaticamente os ordene e exiba
#Sem usar o método sort()

lista = []

for cont in range(0, 5):
    num = int(input('Digite um valor: '))
    if cont == 0 or num > lista[-1]: #se a contagem for igual a zero
        lista.append(num) #ou o número inserido maior que o último valor
    else:
        pos = 0 #posição zero na lista
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
    print(f'Os valores digitados em ordem foram {lista}')