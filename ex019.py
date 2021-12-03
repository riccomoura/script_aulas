import random
aluno1 = input('Digite o nome de um aluno: ')
aluno2 = input('Digite o nome de outro aluno: ')
aluno3 = input('Digite o nome de mais um aluno: ')
aluno4 = input('Digite o nome do último aluno: ')
lista = random.choice([aluno1, aluno2, aluno3, aluno4])
print('O aluno sorteado para ler o enunciado da prova é o(a): {}'.format(lista))
