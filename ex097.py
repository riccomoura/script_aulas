#Faça um programa que tenha uma função escreva()
#Receba um texto qualquer como parâmetro
#Mostre uma mensagem com tamanho adaptável

#Definição da rotina
#Foi criada uma variável "tamanho" que recebe o length da mensagem e aplica a formatação
def escreva(msg):
    tam = len(msg) + 2 #margem dada na soma de 2 caracteres
    print('~' * tam) #impressão da formatação superior multiplicada pelo tamanho da string
    print(f' {msg}') #com a formatação da mensagem definida, dê 1 espaço antes para centralizar
    print('~' * tam)

#Programa principal:
a = str(input('Digite uma mensagem para exibir: '))
escreva(a)