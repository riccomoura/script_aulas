nome = input('Digite seu nome completo e veja a magia acontecer: ')
print('Seu nome completo em uppercase é {}'.format(nome.upper()))
print('Seu nome completo em lowercase é {}'.format(nome.lower()))
print('Seu nome completo possui {} caracteres.'.format(len(nome.replace(" ", ""))))
nomedividido = nome.split()
primeironome = len(nomedividido[0])
print('Seu primeiro nome somente, possui {} caracteres.'.format(primeironome))


