nome = str(input('Digite seu nome: '))
nota1 = float(input('Digite sua nota da AV1: '))
nota2 = float(input('Digite sua nota da AV2: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print('Você está reprovado. Sua média final {} foi abaixo do esperado!'.format(media))
elif 5.0 < media < 6.9:
    print('Você está de recuperação. Sua média final {} pode ser melhorada.'.format(media))
else:
    print('Você está aprovado. Sua média final {} está ótima!'.format(media))