from time import sleep

sleep(1)
print('=== Calculadora de IMC ===')
sleep(1)

nome = str(input('Digite o seu nome: '))
peso = float(input('Digite seu peso: '))
altura = float(input('Digite a sua altura conforme modelo "1.78": '))
imc = peso / altura**2

print('Seu IMC é de {:.1f}. Agora analisaremos a condição.'.format(imc))
sleep(1)
print('...')
sleep(1)

if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 < imc < 25:
    print('Peso Ideal.')
elif 25 < imc < 30:
    print('Sobrepeso')
elif 30 < imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida.')
