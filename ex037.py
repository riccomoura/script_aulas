
n = int(input('Digite um número inteiro: '))
escolha = int(input('Escolha a base de conversão.\n1 para binário\n2 para octal\n3 para hexadecimal\nEscolha >>> '))
bin = 1
octal = 2
hexa = 3

if escolha == 1:
    print('{0:0b}'.format(n))
elif escolha == 2:
    print('{0:2o}'.format(n))
else:
    print('{0:0x}'.format(n))
