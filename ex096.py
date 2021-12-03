#Faça um programa que tenha uma função chamada area()
#Receba as dimensões de um terreno retangular (largura e comprimento)
#Mostre a área do terreno

#Definição da função, cálculo e formatação da rotina
def area(largura, comprimento):
    a = largura * comprimento
    print('-' * 100)
    print(f'A área com {largura} metros de largura e {comprimento} metros de comprimento é de {a} m2.')
    print()
    print(f'Cálculo: {largura} x {comprimento} = {a}')
    print('-' * 100)


#Programa Principal
print('Controle de Terrenos')
largura = float(input('LARGURA: '))
comprimento = float(input('COMPRIMENTO: '))
area(largura, comprimento)