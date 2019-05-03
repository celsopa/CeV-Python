# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

from math import sqrt

n = int(input("Digite um número: "))
print(f"""Analisando o número {n}:
Seu dobro é {n*2}.
Seu triplo é {n*3}.
E sua raiz quadrada é {sqrt(n):.2f}.""")
