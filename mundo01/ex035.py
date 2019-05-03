# Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

from math import fabs
a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))

triangulo = [a, b, c]
triangulo.sort()
print("Analisando os segmentos informados...")
if fabs(b - c) < a < (b + c) and fabs(a - c) < b < (a + c) and fabs(b - a) < c < (b + a):
    print(f"""Os segmentos {a}, {b} e {c} PODEM FORMAR um triângulo.""")
    # Classificação quanto aos lados
    if a == b == c:
        print("O triângulo formado é EQUILÁTERO.")
    elif a != b != c:
        print("O triângulo formado é ESCALENO.")
    else:
        print("O triângulo formado é ISÓSCELES.")
    # Classificação quanto aos ângulos
    if triangulo[2]**2 == triangulo[0]**2 + triangulo[1]**2:
        print("O triângulo formado é RETÂNGULO.")
    elif triangulo[2]**2 > triangulo[0]**2 + triangulo[1]**2:
        print("O triângulo formado é OBTUSÂNGULO.")
    else:
        print("O triângulo formado é ACUTÂNGULO.")

else:
    print(f"""Os segmentos {a}, {b} e {c} NÃO PODEM FORMAR um triângulo.""")
