nome = input('Digite o nome completo do aluno: ')
matr = input('Digite o número de matrícula: ')
n1 = float(input('Digite o valor da AV1: '))
n2 = float(input('Digite o valor da AV2: '))
m = (n1 + n2) / 2
print('O aluno {}, de matrícula {} obteve nesse semestre uma média {:.1f} em suas avalições.'.format(nome, matr, m))