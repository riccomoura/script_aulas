name = input('Digite o nome da sua cidade: ').strip().capitalize()
name = name.split()
busca = name[0].find('Santo')
if (busca != -1):
    print('Sua cidade tem nome de Santo logo no início, né? Que bacana!')
else:
    print('Sua cidade tem lindo nome, mas não começa com "Santo".')

#print(cid(:5).capitalize() == 'Santo')  <<<<<<<<<< também serve.
#print(cid(:5).lower() == 'santo')  <<<<<<<<<< também serve.
#print(cid(:5).upper() == 'SANTO')  <<<<<<<<<< também serve.