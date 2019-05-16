# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input("Digite um número inteiro: "))
div = 0
for d in range(2, n):
    if n % d == 0:
        div += 1
        print("O número não é primo!!!")
        break
if not div:
    print("Esse número é primo!")