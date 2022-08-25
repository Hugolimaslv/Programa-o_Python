"""
Crie uma frase, adicione variaveis e imprima esta frase.
"""

v1 = input('Qual o seu nome? ')
v2 = int(input('Você nasceu em que ano? '))
v3 = input('Qual o nome do seu pai? ')

print(f'Ola {v1.capitalize()}, filho de {v3.title()}. Você tem {2022 - v2} anos.')
