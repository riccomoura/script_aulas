n = input('Digite um valor e obtenha informações sobre seu tipo primitivo entre outras: ')
print('O tipo primitivo do valor é:', type(n))
print('O valor "{}" é numérico?'.format(n), n.isnumeric())
print('O valor "{}" é Alfabético?'.format(n), n.isalpha())
print('O valor "{}" é Alfanumérico?'.format(n), n.isalnum())
print('O valor "{}" é todo "MAIÚSCULO"?'.format(n), n.isupper())
print('O valor "{}" é minúsculo?'.format(n), n.islower())
print('O valor "{}" é decimal?'.format(n), n.isdecimal())
print('O valor "{}" é ASCII?'.format(n), n.isascii())
print('O valor "{}" é dígito?'.format(n), n.isdigit())
print('O valor "{}" é um identificador?'.format(n), n.isidentifier())
print('O valor "{}" é passível de impressão?'.format(n), n.isprintable())
print('O valor "{}" é um espaço?'.format(n), n.isspace())
print('O valor "{}" está capitalizado (primeira letra maiúscula e as outras minúsculas?'.format(n), n.istitle())
