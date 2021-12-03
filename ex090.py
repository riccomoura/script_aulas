#Faça um programa que leia nome e média de um aluno
#Guarde também a situação em um dicionário
#No final, mostre o conteúdo da estrutura na tela

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('-=' * 30)
for k, v in aluno.items():
    print(f' - {k} ==> {v}')