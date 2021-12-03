nome = input('Caro funcionário, digite seu nome: ')
matr = int(input('Agora digite sua matrícula: '))
nprod = input('Agora digite o número do produto em sua etiqueta: ')
p = float(input('Agora digite o valor que consta na etiqueta: '))
desc = p * 0.05
vf = p - desc
print('\nCaro funcionário(a) {}, de matrícula {}.\n\nO produto número {}\n de valor R${: .2f}\n com desconto aplicado de R${: .2f}\n fica no valor final de R${: .2f}.\n\nBoas vendas!'.format(nome, matr, nprod, p, desc, vf))