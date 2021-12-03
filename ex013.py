nome = input('Digite seu nome para descobrir o seu salário a partir do reajuste de sua última promoção: ')
matr = input('Digite sua matrícula para localizarmos seu contrato: ')
salario = float(input('Digite seu salário atual: '))
reajuste = salario * 1.15
print('\n\n{}, seu novo salário, com vencimentos à partir do próximo mês será de {:.2f}, um reajuste total de 15%.\n\nParabéns!'.format(nome, reajuste))