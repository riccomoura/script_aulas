#Exibir a string pelo valor de posição na entrada do usuário

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

for cont in range(0, len(tupla)):
    pos = int(input('Digite a posição: '))
    if pos > 20:
        continue
    else:
        break
print(tupla[pos])