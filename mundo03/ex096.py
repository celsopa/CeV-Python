# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões
# de um terreno retangular (largura e comprimento) e mostre a área do terreno.


def area(largura, comprimento):
    print(f'A área de um terreno de medidas {largura} x {comprimento} é {largura*comprimento}m².')


print('Área de um terreno retangular')
a = float(input('Largura (em metros): '))
b = float(input('Comprimento (em metros): '))
area(a, b)
