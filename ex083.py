#Crie um programa onde o usuário digite uma expressão matemática qualquer que utilize parênteses
#Deverá analisar se a expressão matemática passada está com os parênteses abertos e fechados na ordem correspondente

expr = str(input('Digite a expressão: '))
pilha = [] #utilizando o conceito de pilha para formar pares de parênteses

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está válida.')
else:
    print('Sua expressão está errada.')