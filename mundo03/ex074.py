# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor
# e o maior valor que estão na tupla.

from random import sample

numeros = tuple(sample(range(10), 5))
print(f"Números gerados: {numeros}\n"
      f"Maior valor: {max(numeros)}\n"
      f"Menor valor: {min(numeros)}")