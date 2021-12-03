#Crie um programa que leia nome, ano de nascimento e carteira de trabalho
#Cadastre-os (com idade) em um dicionário se a CTPS for diferente de ZERO
#O dicionário também receberá o ano de contratação e o salário
#Calcule e acrescente, além da idade, com quantos anos a pessoa se aposentará

from datetime import datetime #para calcular aposentadoria com base no ano atual

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (Digite 0 se não tem): '))

#Teste lógico - CTPS
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))

    #Cálculo para estimar idade de aposentadoria a partir da data de contratação
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

#Formatação de Exibição
for k, v in dados.items():
    print(f' - {k} : {v}')