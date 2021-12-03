from time import sleep
from datetime import date
sleep(1)
print('\n=== EXÉRCITO NACIONAL DA REPÚBLICA PYTHONIANA ===')
sleep(2)
(print('\n...'))
sleep(2)
print('\n=== PROGRAMA DE CONSULTA - QUITAÇÃO DE SERVIÇO MILITAR ===')
sleep(2)

nome = str(input('\nDigite seu nome: '))
nasc = int(input('\nDigite o ano do seu nascimento: '))

(print('...'))
sleep(2)

data_atual = date.today()
data_atual_texto = '{}'.format(data_atual.year)
idade = data_atual.year - nasc
prevalist = 18 - idade

if idade < 18:
    print('Caro patriota, ainda falta(m) {} ano(s) para seu alistamento.'.format(prevalist))
elif 18 < idade < 22:
    print('Você está apto ao serviço militar, mas consta atraso na sua data de alistamento.')
    sleep(1)
    print('Se você já cumpriu seu serviço militar e não possui certificado de reservista...')
    sleep(1)
    print('... entre em contato com a junta regional da sua cidade.'.format(data_atual.year))
    sleep(2)
    print('A idade máxima para alistar-se é até os 21 anos de idade.')
elif idade == 18:
    print('Você está apto ao alistamento!')
    sleep(1)
    print('O descumprimento das obrigações militares dentro do prazo acarreta consequências.')
    sleep(1)
    print('Podem incidir multas e penalidades militares previstos por lei.')
else:
    (print('Você já deve ser um reservista, certo? Senão, regularize sua situação o mais breve possível.'))
    sleep(1)
    print('Consulte a junta militar mais próxima para quitação de eventuais documentos arrecadatórios e multas.')






