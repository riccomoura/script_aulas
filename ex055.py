max = 0
min = 0

for p in range(1, 6):
    peso = float(input('Digite o peso da {}a pessoa: '.format(p)))
    if p == 1:
        max = peso
        min = peso
    else:
        if peso > max:
            max = peso
        if peso < min:
            min = peso

print('O maior peso lido foi de {}Kg'.format(max))
print('O menor peso lido foi de {}Kg'.format(min))








