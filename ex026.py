name = input('Digite uma frase favorita: ').lower().strip().replace(" ","")
print('A frase possui {} caracteres.'.format(len(name)))
contagem = name.count('a')
busca1 = name.find('a')
busca2 = name.rfind('a')
print('A letra "A" aparece {} vezes, sendo a primeira na posição {} e última na posição {}.'.format(contagem, busca1, busca2))
