nome = input('Qual é o seu nome? ')
l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))
area = l * a
tinta = area / 2
print('{}, você precisará de {:.2f} litros de tinta pra concluir a pintura da área total de {:.2f} metros quadrados.'.format(nome, tinta, area))