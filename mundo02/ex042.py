# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo
# de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

from math import fabs
a = int(input("Primeiro segmento: "))
b = int(input("Segundo segmento: "))
c = int(input("Terceiro segmbento: "))

print("Analisando os segmentos informados...")
if fabs(b - c) < a < (b + c) and fabs(a - c) < b < (a + c) and fabs(b - a) < c < (b + a):
    print(f"""Os segmentos {a}, {b} e {c} PODEM FORMAR um triângulo""", end=" ")
    # Classificação quanto aos lados
    if a == b == c:
        print("EQUILÁTERO.")
    elif a != b and a != c and b != c:
        print("ESCALENO.")
    else:
        print("ISÓSCELES.")
else:
    print(f"""Os segmentos {a}, {b} e {c} NÃO PODEM FORMAR um triângulo.""")