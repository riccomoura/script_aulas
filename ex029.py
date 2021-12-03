import math
vm = int(input('Digite a suposta velocidade atual do veículo: '))
multa = (vm - 80) * 7
if vm > 80:
    print('Velocidade máxima permitida de 80km/h. A multa aplicada será de: R${}'.format(multa))
else:
    print('Parabéns, mantenha-se abaixo do limite de velocidade. Preserve a vida.')