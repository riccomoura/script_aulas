from time import sleep
sleep(1)
print('Agora será exibido na tela uma contagem...')
sleep(1)
print('Essa contagem exibirá somente números pares entre 1 e 50...')
for c in range(1, 51):
    if c%2==0:
        print(c)

'''
Método otimizado com metade das interações:

from time import sleep
sleep(1)
print('Agora será exibido na tela uma contagem...')
sleep(1)
print('Essa contagem exibirá somente números pares entre 1 e 50...')
for c in range(2, 51, 2):
    print(c)
    
    '''