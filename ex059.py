n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opt = 0

while opt != 5:
    print('''  [ 1 ] - Somar
    [ 2 ] - Multiplicar
    [ 3 ] - Mostrar maior valor
    [ 4 ] - Digitar novos números
    [ 5 ] - Sair do programa''')
    opt = int(input('Qual é sua opção? '))
    if opt == 1:
      soma = n1 + n2
      print('A soma entre {} e {} é = {}'.format(n1, n2, soma))
    elif opt == 2:
      produto = n1 * n2
      print('O resultado entre {} e {} é = {}'.format(n1, n2, produto))
    elif opt == 3:
      if n1 > n2:
        maior = n1
      else:
        maior = n2
      print('Entre {} e {}, o maior valor é = {}'.format(n1, n2, maior))
    elif opt == 4:
      print('Informe os números novamente: ')
      n1 = int(input('Primeiro valor: '))
      n2 = int(input('Segundo valor: '))
    elif opt == 5:
      print('Finalizando...')
    else:
      print('Opção inválida. Tente novamente.')
      print('=-=' * 10)
print('Fim do programa! Volte Sempre!')