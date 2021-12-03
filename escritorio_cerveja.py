from time import sleep

sleep(1)
print('=== TERMINAL DE IDENTIFICAÇÃO E COLETA DE PEDIDO ===')
sleep(1)
empregado = int(input('Colaborador, se você for o Marcelo Juliano, digite 1(um).\nSenão, digite 0(zero): '))
sleep(1)
if empregado == 1:
    print('Serve um bom café!')
    quit()
else:
    nome = str(input('Digite o seu nome: '))
sleep(2)
cerveja = int(input('''
Digite o número correspondente à cerveja que deseja:
LOKAL [0]
BRAHMA [1]
ITAIPAVA [2]
BOHEMIA [3]
SKOL [4]
GLACIAL [5]
HEINEKEN [6]
'''))
if cerveja == 0:
    print('Tá de sacanagem? Nem se tivéssemos ela seria disponibilizada.')
    quit()
elif cerveja == 5:
    print('Fora de estoque. Graças a Deus.')
    quit()
else:
    print('OK')
sleep(1)
print('Leve até a sala do Charles do Carmo.')