import random

aluno1 = input('Digite o nome de um aluno: ')
aluno2 = input('Digite o nome de outro aluno: ')
aluno3 = input('Digite o nome de mais um aluno: ')
aluno4 = input('Digite o nome do último aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)

print('O Aluno escolhido foi {}'.format(escolhido))