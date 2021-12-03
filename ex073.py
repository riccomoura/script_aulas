#Tupla de times de futebol - Uso de INDEX e interpolação

times = ('Atlético - MG',
    'Palmeiras',
    'Flamengo',
    'Fortaleza',
    'Bragantino',
    'Corinthians',
    'Fluminense',
    'Cuiabá',
    'Internacional',
    'Atlético - GO',
    'Athlético - PR',
    'Ceará SC',
    'Santos',
    'Juventude',
    'Bahia',
    'São Paulo',
    'América - MG',
    'Grêmio',
    'Sport Recife',
    'Chapecoense'
)

#Exibindo os cinco primeiro colocados do Brasileirão
print(" " * 2)
print('Os primeiros cinco colocados no campeonato são, respectivamente >>>>\n')
print(times[:5])

#Os quatro últimos colocados no Brasileirão
print(" " * 2)
print('Os quatro últimos colocados no campeonato são, respectivamente >>>>\n')
print(times[-4:])

#Segue abaixo uma lista em ordem alfabética dos times da Série A
print(" " * 2)
print('Segue abaixo uma lista em ordem alfabética dos times da Série A:\n')
print(sorted(times))

#A posição do Cuiabá no Brasileirão
print(" " * 2)
print(f'O Cuiabá está na {times.index("Cuiabá")+1}a posição.')
#Usar as aspas duplas no index dentro de aspas simples do print() para fazer a interpolação

print(" " * 3)