i = int(input('Digite um número para iniciar uma contagem: '))
f = int(input('Digite um número para finalizar a contagem: '))
p = int(input('Digite o ordenamento preferencial. Ex.: "2" para "2 em 2": '))

for c in range(i, f-1, -p):
    print(c)
print('FIM DO REVERSO')