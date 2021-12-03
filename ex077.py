#Mostrar as vogais sem acentuação que existem dentro das tuplas

#Crie um programa que tenha uma tupla com várias palavras.
#Depois, mostre para cada palavra, quais são suas vogais.

palavras = ('aprender',
            'programar',
            'linguagem',
            'python',
            'curso',
            'gratis',
            'estudar',
            'praticar',
            'trabalhar',
            'mercado',
            'programador',
            'futuro'
            )

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos - sem acentos - as vogais ', end='')
    #Função Upper para destacar as palavras
    for letra in p:
        if letra.lower() in 'aeiou': #Função Lower() para evitar conflitos case sensitive
            print(letra, end=' / ')