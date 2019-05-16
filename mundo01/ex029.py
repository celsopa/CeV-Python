# Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Informe a velocidade do carro: '))
if vel > 80:
    print(f'''Você ultrapassou o limite de velocidade em {vel-80}km/h.
Você foi multado em R${(vel-80)*7:.2f}! Reduza sua velocidade!''')
else:
    print(f'Continue respeitando o limite de velocidade.')