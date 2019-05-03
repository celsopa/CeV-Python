# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))
menor = a
maior = a

if b < menor:
    menor = b
if c < menor:
    menor = c
if b > maior:
    maior = b
if c > maior:
    maior = c
print(f"""Analisando os números {a}, {b} e {c}:
O MAIOR número é: {maior}.
O MENOR número é: {menor}.""")

