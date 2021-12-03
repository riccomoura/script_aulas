n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
if n1 > n2 and n3:
    print('O número {} é o maior.'.format(n1))
    if n2 > n1 and n3:
        print('O número {} é o maior.'.format(n2))
    else:
        print('O número {} é o menor.'.format(n3))
if n1 < n2 and n3:
    print('O número menor é {}.'.format(n1))
    if n2 < n1 and n3:
        print('O número menor é {}'.format(n2))
    else:
        print('O número maior é {}'.format(n3))