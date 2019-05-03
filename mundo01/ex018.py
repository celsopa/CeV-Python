# Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

graus = float(input("Informe a medida do ângulo: "))
rad = radians(graus)
print(f"""Um ângulo de {graus:.2f}º possui:
seno     = {sin(rad):.2f}
cosseno  = {cos(rad):.2f}
tangente = {tan(rad):.2f}""")
