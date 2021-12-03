#MÉTODO RÁPIDO

n = int(input("Insira o valor inicial da Progressão Aritmética: "))
r = int(input("Insira um valor para a razão: "))

for c in range(0, 10):
    print(n)
    n = n+r
'''
MÉTODO DE CORNO

#Insira o primeiro termo e a razão de uma PA, exibindo os 10 primeiros termos.

a = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

#Progressão Aritmética
#Fórmula: primeiro termo + (número de termos - 1) * razão
d = a + (10 - 1) * r #aplicação da fórmula

#Contagem do primeiro termo a progressão, tendo a razão como regra.
for c in range(a, d + 1, r):
    print(c)
'''

'''Essencialmente o algoritmo pede uma contagem do primeiro ao ultimo termo
passando como regra de contagem sua razão.
onde a progressão é o último termo (décimo), exibindo todos os anteriores pulando de regra em regra.'''